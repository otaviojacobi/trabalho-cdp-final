from bisect import bisect_left, bisect_right
import sys
import pickle

class BPTree(object):
	def __init__(self, capacity):
		''' create an empty BPTree where each node has
		capacity keys and capacity+1 pointers.
		Each leaf has capacity keys. '''

		self._tree=BPTreeLeaf([],None, capacity)
		self._capacity=capacity

	def insert(self, key):
		''' insert key into our subtree '''
		pkey, ppointer = self._tree.insert(key)
		if pkey is not None:
			new_master_node = BPTreeNode([pkey], [self._tree, ppointer], self._capacity)
			self._tree = new_master_node

	def keys(self):
		''' return a list of all keys in self '''
		return self._tree.keys()

	def find(self, key):
		''' return whether key is in this BPTree '''
		return self._tree.find(key)

	def find_range(self, key, dir):
		return self._tree.find_range(key, dir)

	def num_nodes(self):
		return self._tree.num_nodes()

	def num_leaves(self):
		return self._tree.num_leaves()

	def num_keys(self):
		return self._tree.num_keys()

	def height(self):
		return self._tree.height() + 1

	def stats(self):
		''' return a tuple consisting of (height, number of nodes, number of keys, number of leaves) in the tree '''
		return (self.height(), self.num_nodes(), self.num_leaves(), self.num_keys())

	def __str__(self):
		'''For visualization purposes'''
		s = ""
		for level in range(1, self.height() + 1):
			if level == 1:
				s += ' '*self.num_keys()*2 + str(self._tree)
			elif level == self.height():
				leaf = self._tree._pointers[0]
				for i in range(self.height()-2):
					leaf = leaf._pointers[0]

				while leaf._next is not None:
				       s += str(leaf)+"->"
				       leaf = leaf._next
				s += str(leaf)
			elif level == 2:
				s += ' '*self.num_keys()
				for child in self._tree._pointers:
					s+= str(child) + " "
			elif level == 3:
				s += ' '*self.num_keys()
				for child in self._tree._pointers:
					for kid in child._pointers:
						s+= str(kid) + " "
			s += "\n"
		return s

	def getRange(self, lo, hi, dataflag = 0):
		flaginverte = 0

		resultado = []
		if dataflag == 0:
		    aux=str(float(lo)).split('.', 1)
		    aux[0] = aux[0].zfill(3)
		    lo = aux[0] + '.' + aux[1]
		    #print(lo)
		    aux=str(float(hi)).split('.', 1)
		    aux[0] = aux[0].zfill(3)
		    hi = aux[0] + '.' + aux[1]
		    if lo > hi:
		        lo,hi = hi,lo
		        flaginverte = 1
		    #print(hi)
		if dataflag == 1:
		    aux = str(lo).split('/', 2)
		    lo = aux[2] + '/' + aux[1] + '/' + aux[0]
		    aux = str(hi).split('/', 2)
		    hi = aux[2] + '/' + aux[1] + '/' + aux[0]
		    if lo > hi:
		        lo,hi = hi,lo
		        flaginverte = 1
		lowleaf, lowindex = self.find_range(lo, 'low')
		#print("oe", lowleaf)
		highleaf, highindex = self.find_range(hi, 'high')
		#print("eita", highleaf)
		if lowleaf == highleaf:
		    if highindex == 0 or lowindex is None:
		        return resultado
		    elif highindex == lowindex:
		        return resultado
		    else:
		        resultado = resultado + lowleaf._keys[lowindex:highindex]
		        if flaginverte == 1:
		            resultado.reverse()
		        return resultado
		if lowindex != 0:
		    resultado = resultado + lowleaf._keys[lowindex:]
		    lowleaf = lowleaf._next
		if lowindex is None:
		    lowleaf = lowleaf._next
		while lowleaf != highleaf:
		    resultado = resultado + lowleaf._keys
		    lowleaf = lowleaf._next
		if lowleaf == highleaf:
		    resultado = resultado + lowleaf._keys[lowindex:highindex]
		    if flaginverte == 1:
		        resultado.reverse()
		    return resultado



class BPTreeNode(object):
	def __init__(self, keys, pointers, capacity):
		''' New BPTreeNode with keys=[key0,key1,..., keyK], pointers=[pointer0, pointer1,...,pointerK+1] '''

		self._keys = keys # in sorted order
		self._pointers = pointers # one more than the number of keys
		self._capacity = capacity

	def keys(self):
		''' return a list of all keys in the leaves of this subtree '''
		return self._pointers[0].keys()

	def find(self, key):
		''' return whether key is in this tree (at the appropriate leaf) '''
		return self._pointers[bisect_right(self._keys, key)].find(key)

	def find_range(self, key, dir):
	    return self._pointers[bisect_right(self._keys, key)].find_range(key, dir)

	def insert_here(self, position, key, pointer): #inserting at node level
		''' insert key, at 'position' and pointer at 'position+1'
		return (None, None) if there is nothing to promote
		return (pkey, ppointer) if self splits,
		(pkey, ppointer) this is the promoted key, and,
		a pointer to the newly created BPTreeNode '''
		self._keys.insert(position, key)
		self._pointers.insert(position+1, pointer)

		cap = self._capacity
		split_index = (cap + 1)//2
		if len(self._keys) > cap:
			pkey = self._keys[split_index]
			self._keys.remove(pkey)

			new_lateral_node = BPTreeNode(self._keys[split_index:], self._pointers[split_index + 1:], cap)

			self._keys = self._keys[:split_index]
			self._pointers = self._pointers[:split_index + 1]

			return (pkey, new_lateral_node)
		return (None, None)

	def insert(self, key):
		''' insert key into this subtree
		return (None, None) if there is nothing to promote
		return (pkey, ppointer) if self splits '''

		# Insert down correct path
		(pkey, ppointer) = self._pointers[bisect_right(self._keys, key)].insert(key)

		# Handle promotions
		if pkey is not None:
			position = bisect_left(self._keys, pkey)
			(promoted_key, new_lateral_node) = self.insert_here(position, pkey, ppointer)
			return (promoted_key, new_lateral_node)
		return (None, None)

	def num_nodes(self):
		''' Number of nodes in this subtree including this one'''
		# Sum of num_nodes of each child plus 1
		return 1 + sum(map(lambda n: n.num_nodes(), self._pointers))

	def num_leaves(self):
		''' number of leaves in this subtree'''
		# Sum of num_leaves of each child
		return sum(map(lambda n: n.num_leaves(), self._pointers))

	def num_keys(self):
		''' number of keys in the leaves of this subtree'''
		# Map num_keys to each child node then sum the results
		return sum(map(lambda n: n.num_keys(), self._pointers))

	def height(self):
		''' height of this subtree'''
		return 1 + self._pointers[0].height()

	def __str__(self):
		return str(self._keys)


class BPTreeLeaf(object):
	def __init__(self, keys, next_leaf, capacity):
		self._keys = keys # in sorted order
		self._next = next_leaf # next BPTreeLeaf
		self._capacity = capacity

	def keys(self):
		''' return a list of all keys from here to the end of the linked list of BPTreeLeaf '''
		all_keys = []
		for element in self._keys:
			all_keys.append(element)
		current = self
		while current._next is not None:
			current = current._next
			all_keys.extend(current._keys)
		return all_keys


	def find(self, key):
		''' return whether key is in this leaf '''
		listachaves=[]
		for chave in self._keys:
			listachaves.append(chave.split('$',1)[0])
		if key in listachaves:
			return self
		else:
			return None

	def find_range(self, key, dir):
		''' acha um dos limites de um determinado range '''
		if dir == 'low':
			if bisect_left(self._keys, key) >= len(self._keys):
				return self, None
			else:
				return self, bisect_left(self._keys, key)
		if dir == 'high':
				return self, bisect_right(self._keys, key)

	def insert(self, key):
		''' insert key into self. A key should not appear twice in the BPTreeLeaf level
		return (None, None) if there is nothing to promote
		return (pkey, ppointer) if self splits
		(pkey, ppointer) this is the promoted key, and,
		a pointer to the newly created '''
		#on
		index = bisect_left(self._keys, key)
		if index == len(self._keys) or self._keys[index] != key:
			self._keys.insert(index, key)

		cap = self._capacity
		split_index = (cap+1)//2

		if len(self._keys) > cap:
			new_leaf = BPTreeLeaf(self._keys[split_index:], self._next, cap)

			self._keys = self._keys[:split_index]
			self._next = new_leaf

			return (new_leaf._keys[0], new_leaf)
		return (None, None)

	def num_nodes(self):
		return 0

	def num_leaves(self):
		return 1

	def num_keys(self):
		return len(self._keys)

	def height(self):
		return 0

	def __str__(self):
		return str(self._keys)

'''
Insere do arquivo .csv com as colunas corretas
'''
def insere_from_file(arquivo):
    t=100
    chuva=BPTree(t)
    tempM=BPTree(t)
    tempm=BPTree(t)
    sol=BPTree(t)
    umidade=BPTree(t)
    vento=BPTree(t)
    data=BPTree(t)


    fopen=open(arquivo,'r')

    lista=[]
    for line in fopen:
        if 'E' not in line:
            linha=line.split(',')
            lista.append([linha[0]+linha[1]]+linha[2:])

    lis_chuva=[]
    lis_tempM=[]
    lis_tempm=[]
    lis_sol=[]
    lis_umidade=[]
    lis_vento=[]
    lis_data=[]
    for row in lista:
        _chuva=row[1].strip('\n')
        try:
            _chuva=str(float(_chuva))
            _chuva=_chuva.split('.')
            lis_chuva.append('.'.join([_chuva[0].zfill(3),_chuva[1].ljust(6,'0')])+'$'+row[0])
        except:
            pass

        _tempM=row[2].strip('\n')
        try:
            _tempM=str(float(_tempM))
            _tempM=_tempM.split('.')
            lis_tempM.append('.'.join([_tempM[0].zfill(3),_tempM[1].ljust(6,'0')])+'$'+row[0])
        except:
            pass

        _tempm=row[3].strip('\n')
        try:
            _tempm=str(float(_tempm))
            _tempm=_tempm.split('.')
            lis_tempm.append('.'.join([_tempm[0].zfill(3),_tempm[1].ljust(6,'0')])+'$'+row[0])
        except:
            pass

        _sol=row[4].strip('\n')
        try:
            _sol=str(float(_sol))
            _sol=_sol.split('.')
            lis_sol.append('.'.join([_sol[0].zfill(3),_sol[1].ljust(6,'0')])+'$'+row[0])
        except:
            pass

        _umidade=row[5].strip('\n')
        try:
            _umidade=str(float(_umidade))
            _umidade=_umidade.split('.')
            lis_umidade.append('.'.join([_umidade[0].zfill(3),_umidade[1].ljust(6,'0')])+'$'+row[0])
        except:
            pass

        _vento=row[6].strip('\n')
        try:
            _vento=str(float(_vento))
            _vento=_vento.split('.')
            lis_vento.append('.'.join([_vento[0].zfill(3),_vento[1].ljust(6,'0')])+'$'+row[0])
        except:
            pass

        _data=row[0].strip('\n')
        try:
            x = _data.split('/')
            _data = '/'.join([x[2],x[1],x[0][5:]])
            mega_string = _data + '$' + x[0][0:5] +','+ ','.join([row[1],row[2],row[3],row[4],row[5],row[6].strip('\n')])
            lis_data.append(mega_string)
        except:
            pass


    for chave in lis_chuva:
        chuva.insert(chave)
    for chave in lis_tempM:
        tempM.insert(chave)
    for chave in lis_tempm:
        tempm.insert(chave)
    for chave in lis_sol:
        sol.insert(chave)
    for chave in lis_umidade:
        umidade.insert(chave)
    for chave in lis_vento:
        vento.insert(chave)
    for chave in lis_data:
        data.insert(chave)

    return chuva, tempM, tempm, sol, umidade, vento, data


def save_parameters(chuva,tempM,tempm, sol,umidade, vento, data):
    sys.setrecursionlimit(4000)
    afile=open('g_dados.bin','wb')
    pickle.dump(chuva,afile,1)
    pickle.dump(tempM,afile,1)
    pickle.dump(tempm,afile,1)
    pickle.dump(sol,afile,1)
    pickle.dump(umidade,afile,1)
    pickle.dump(vento,afile,1)
    pickle.dump(data,afile,1)
    afile.close()

def load_stuff(arquivo):
    novo_file=open(arquivo,'rb')
    chuva_loaded = pickle.load(novo_file)
    tempM_loaded = pickle.load(novo_file)
    tempm_loaded = pickle.load(novo_file)
    sol_loaded = pickle.load(novo_file)
    umidade_loaded = pickle.load(novo_file)
    vento_loaded = pickle.load(novo_file)
    data_lodaded = pickle.load(novo_file)
    novo_file.close()

    return chuva_loaded, tempM_loaded, tempm_loaded, sol_loaded, umidade_loaded, vento_loaded, data_lodaded
