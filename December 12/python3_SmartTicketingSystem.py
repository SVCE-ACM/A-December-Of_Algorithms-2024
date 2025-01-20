# December 12 - Smart Ticketing System


# Total no of tickets 
T = int(input("Enter the total number of tickets: "))

# Requests
print("Enter the requests in the following format, \nJohn 3 VIP, Alice 2, Bob 3")
r = list(map(str.strip, input().split(",")))

# Normal and VIP people
np = []
vp = []

# Purhase history
ph = []

for p in r:
	# Seperated Details
	sd = p.split()
	name = sd[0]
	tickets = sd[1]
	
	if "VIP" in p:
		vp.append([name, tickets])
	else:
		np.append([name, tickets])

def process(person):
	
	global T
	
	if T > 0:
		# Requested Tickets
		rt = int(person[1])
	
		# Here person[1] acts as 'allocated tickets'
		if T-rt < 0:
			person[1] = T
			T = 0
		else:
			p[1] = rt
			T -= rt
	
		ph.append("{} purchased {} tickets".format(person[0], person[1]))
		
	else:
		ph.append("{} was not served".format(person[0]))

# Processing VIPs first
for p in vp:
	process(p)

# Processing others
for p in np:
	process(p)
	
print(ph)


""" Solution from 1012 """