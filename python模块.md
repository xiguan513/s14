## range
	函数原型：range（start， end， scan):

       -- 参数含义：

			  start:计数从start开始。默认是从0开始。例如range（5）等价于range（0， 5）;
              end:  计数到end结束，但不包括end.例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
              scan：每次跳跃的间距，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
			  如果结束数为负数，必须指定跳跃数
			  python3 中range作为一个迭代函数，需要指定list转换下对象关系
		-- 例子：
				>>> list(range(4,-4,-1))
				[4, 3, 2, 1, 0, -1, -2, -3]
				>>> list(range(5,-1,-1))
				[5, 4, 3, 2, 1, 0]
				>>> list(range(5,-1))
				[]
				>>> list(range(5,-5))
				[]
				>>> range(5)
				range(0, 5)
				>>> list(range(5))
				[0, 1, 2, 3, 4]
				>>> list(range(0,5))
				[0, 1, 2, 3, 4]
				>>> list(range(0,5,2))
				[0, 2, 4]
				>>> list(range(5,-1))
				[]
				>>> list(range(5,-1,-2))
				[5, 3, 1]
				>>> list(range(5,-1,-1))
				[5, 4, 3, 2, 1, 0]
				>>> list(range(5,-3,-1))
				[5, 4, 3, 2, 1, 0, -1, -2]

		--不用set集合方法，去除列表中的重复元素

			方法一：
				使用对比类别元素方法，删除重复元素
				List=['b','b','d','b','c','a','a','d','d','d','e']
				print "the list is:",List
				if List:
				    List.sort()#排序
				    print "排序以后输出： %s" % List
				    last=List[-1]#取最后一个值
				    print "输出list的长度",len(List)
				    for i in range(len(List)-2,-1,-1):#倒数的方法带入列表
				        print "输出i=",i
				        print "输出list对应的i的值：",List[i]
				        if last==List[i]:
				            del List[i]
				            print "删除以后的List",List
				        else:
				            last=List[i]
				            print "输出last的值", last
				
				print "after deleting the repreted element the list is :" ,List
			方法2：
				使用类别表达式方法判断去重复
				l2=[]
				[l2.append(i) for i in List if not i in l2]
				print l2
##uuid 获取ip Mac 主机名

			import uuid
			def get_mac_address():
			    mac=uuid.UUID(int=uuid.getnode()).hex[-12:]
			    return ":".join([mac[e:e+2] for e in range(0,11,2)])
			print get_mac_address()
			
			import socket
			
			myname=socket.getfqdn(socket.gethostname( ))
			myaddr=socket.gethostbyname(myname)
			print myname
			print myaddr
#collections 包含多容器数据类型
	counter是一个计数器，它可以帮助我们针对某项数据进行计数

			from  collections import Counter
			
			colours=(
			    ('Yasoob','Yellow'),
			    ('Ali','Blue'),
			    ('Arham','Green'),
			    ('Ali','Black'),
			    ('Yasoob','Red'),
			    ('Ahemd','Silver'),
			)
			
			favs=Counter(name for name,colour in colours)
			print favs
			
		输出结果：
			Counter({'Yasoob': 2, 'Ali': 2, 'Arham': 1, 'Ahemd': 1})


	
	defaultdict
			'''defaultdict 主要用来需要对 value 做初始化的情形。对于字典来说，key 必须是 hashable，immutable，unique 的数据，而 value 可以是任意的数据类型。如果 value 是 list，dict 等数据类型，在使用之前必须初始化为空，有些情况需要把 value 初始化为特殊值，比如 0 或者 '''

			from collections import defaultdict
			colours=(
			    ('Yasoob','Yellow'),
			    ('Ali','Blue'),
			    ('Arham','Green'),
			    ('Ali','Black'),
			    ('Yasoob','Red'),
			    ('Ahemd','Silver'),
			)
			
			favourite_colours=defaultdict(list)#初始化字典valuse为空列表
			for name,colour in colours:
			favourite_colours[name].append(colour)
			print favourite_colours


	  输出结果：
			defaultdict(<type 'list'>, {'Arham': ['Green'], 'Yasoob': ['Yellow', 'Red'], 'Ahemd': ['Silver'], 'Ali': ['Blue', 'Black']})

	deque
			使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。
			In [8]: d=deque([1,2,3],maxlen=3)
			In [9]: d
			Out[9]: deque([1, 2, 3])
			In [10]: d.append('t')
			In [11]: d.append('s')
			In [12]: d
			Out[12]: deque([3, 't', 's'])
			In [13]: d.appendleft('song')
			In [14]: d
			Out[14]: deque(['song', 3, 't'])
			In [15]: d.pop()
			Out[15]: 't'
			In [16]: d
			Out[16]: deque(['song', 3])
			In [17]: d.popleft()
			Out[17]: 'song'
			In [18]: d
			Out[18]: deque([3])


			#!/usr/bin/env python
			# -*- coding: UTF-8 -*-
			
			from collections import deque
			
			
			#定义函数search，并接收三个参数，文件，关键字，历史记录的行数
			def search(lines,pattern,history=5):
			    previous_lines=deque(maxlen=history) #使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除掉。
			    for li in lines:
			        if pattern in li:
			            yield li,previous_lines
			        previous_lines.append(li)
			
			if __name__=='__main__':
			    with open(r'somefile.txt') as f:
			        for line,prelines in search(f,'python',5):#此处search(f,'python',5) 返回yield的值（li,previous_lines）
			            for pline in prelines:
			                print(pline,end='')
			            print(line,end='')
			            print('-'*20)
	
	OrderedDict
			#在迭代操作的时候它会保持元素被插入时的顺序
			#rderedDict 内部维护着一个根据键插入顺序排序的双向链表。每次当一个新的元素插入进来的时候， 它会被放到链表的尾部。对于一个已经存在的键的重复赋值不会改变键的顺序。
			#需要注意的是，一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维护着另外一个链表。
			from collections import OrderedDict
			
			t=OrderedDict()
			t['foo']=1
			t['bar']=2
			t['spam']=3
			t['foo']=4
			
			for key in t:
			    print(key,t[key])
		输出结果：
			foo 4
			bar 2
			spam 3
		 
##enumberate枚举

		my_list = ['apple', 'banana', 'grapes', 'pear']
		for c, value in enumerate(my_list, 1):
    		print(c, value)

		输出结果：
			(1, 'apple')
			(2, 'banana')
			(3, 'grapes')
			(4, 'pear')


##heapq

		heapq模块有两个函数：nlargest() 和 nsmallest() 从集合中获得最大或者最小的N个元素列表
		import heapq

		nums=[1,9,2,3,43,23,95,53,88,-1,100,-5]
		
		print(heapq.nlargest(3,nums))
		print(heapq.nsmallest(3,nums))


		
		#!/usr/bin/env python
		# -*- coding: UTF-8 -*-
		
		
		#heapq模块有两个函数：nlargest() 和 nsmallest() 从集合中获得最大或者最小的N个元素列表
		
		import heapq
		# nums=[1,9,2,3,43,23,95,53,88,-1,100,-5]
		# print(heapq.nlargest(3,nums))
		# print(heapq.nsmallest(3,nums))
		

		#实现了一个简单的优先级队列
		class PrioriyQueue:
		    def __init__(self):
		        self._queue=[]
		        self._index=0
		
		    def push(self,item,priority):
		        heapq.heappush(self._queue,(-priority,self._index,item))
		        self._index+=1
		
		    def pop(self):
		        return heapq.heappop(self._queue)[-1]
		
		class Item:
		    def __init__(self,name):
		        self.name=name
		
		    def __repr__(self):
		        return 'Item({!r})'.format(self.name)
		
		q=PrioriyQueue()
		q.push(Item('foo'),1)
		q.push(Item('bar'),5)
		q.push(Item('spam'),4)
		q.push(Item('grok'),1)
		print(q.pop())
		print(q.pop())
		print(q.pop())
		print(q.pop())

		#第一个 pop() 操作返回优先级最高的元素。 另外注意到如果两个有着相同优先级的元素( foo 和 grok )，pop操作按照它们被插入到队列的顺序返回的。


##sorted
		sorted(iterable[,cmp,[,key[,reverse=True]]])
		作用：返回一个经过排序的列表。
		第一个参数是一个iterable，返回值是一个对iterable中元素进行排序后的列表(list)。
		可选的参数有三个，cmp、key和reverse。
		1)cmp指定一个定制的比较函数，这个函数接收两个参数（iterable的元素），如果第一个参数小于第二个参数，返回一个负数；如果第一个参数等于第二个参数，返回零；如果第一个参数大于第二个参数，返回一个正数。默认值为None。
		2)key指定一个接收一个参数的函数，这个函数用于从每个元素中提取一个用于比较的关键字。默认值为None。
		3)reverse是一个布尔值。如果设置为True，列表元素将被倒序排列。
		key参数的值应该是一个函数，这个函数接收一个参数并且返回一个用于比较的关键字。对复杂对象的比较通常是使用对象的切片作为关键字。
			
			dict1={9:2,
			       3:4,
			       5:1,
			       "a":"c",
			       "e":"b",
			       "*":"$"}
			#print dict1
			#以字典的key排序
			print sorted(dict1.items(),key=lambda x:x[0])
			#以字典的值排序
			print sorted(dict1.items(),key=lambda x:x[1])

##zip

	把两个列表按照最短类别合并
		a=range(10)
		b=range(10,20)
		print zip(a,b)
		输出结果：
		[(0, 10), (1, 11), (2, 12), (3, 13), (4, 14), (5, 15), (6, 16), (7, 17), (8, 18), (9, 19)]
