from clib import *
import data
import inflect

def _001():
	ans = 0
	for i in range(1000):
		ans += i if i % 3 == 0 or i % 5 == 0 else 0
	return ans

def _002():
	ans = 0
	fib = a = 0
	b = 1
	while fib < 4e6:
		fib = a + b
		a = b
		b = fib
		ans += fib if fib % 2 == 0 else 0
	return ans

def _003():
	ans = 0
	limit = 600851475143

	for i in range(1, int(sqrt(limit))):
		if limit % i == 0:
			ans = i
			limit /= i

	if ans < limit:
		ans = limit
	return ans

def _004():
	ans = 0
	for a in range(100, 1000):
		for b in range(100, 1000):
			c = a * b
			if is_palindrome(c) and ans < c:
				ans = c
	return ans

def _005():
	ans = 0
	number = 80
	while True:
		if(is_smallest_multiple(number)):
			ans = number
			break
		number += 80
	return ans

def _006():
	ans = 0
	square_sum = sum_square = 0

	for i in range(101): 
		sum_square += ( i * i )

	for i in range(101):
		square_sum += i
	square_sum *= square_sum

	ans = square_sum - sum_square
	return ans

def _007():
	ans = 0
	ans = 3
	numPrimes = 1
	while True:
		if is_prime(ans):
			numPrimes += 1
			if numPrimes == 10001:
				break
		ans += 2
	return ans

def _008():
	ans = 0
	numbers = data._008
	for i in range(len(numbers) - 12):
		subSection = numbers[i:i + 13]
		product = mult(map(int, subSection))
		if product > ans:
			ans = product
	return ans

def _009():
	ans = 0
	for a in range(500):
		for b in range(333):
			c = 1000 - a - b
			if a * a + b * b == c * c:
				ans = a * b * c
	return ans

def _010():
	return sum(sieve(2000000))

def _011():
	ans = None
	return ans

def _012():
	ans = 0
	i = 1
	while True:
		ans += i
		i += 1
		if num_divisors(ans) >= 500:
			break
	return ans

def _013():
	ans = 0
	numbers = data._013
	ans = int(str(sum(numbers))[0:10])
	return ans

def _014():
	ans = None
	return ans

def _015():
	return int(factorial(40) / (factorial(20) * factorial(20)))

def _016():
	return sum(map(int, str(2**1000)))

def _017():
	ans = 0
	p = inflect.engine()
	for i in range(1000):
		ans += len(p.number_to_words(i + 1).replace(' ', '').replace('-', ''))
	return ans

def _018():
	ans = None
	return ans

def _019():
	ans = None
	return ans

def _020():
	ans = None
	return ans

def _021():
	ans = None
	return ans

def _022():
	ans = None
	return ans

def _023():
	ans = None
	return ans

def _024():
	ans = None
	return ans

def _025():
	ans = None
	return ans

def _026():
	ans = None
	return ans

def _027():
	ans = None
	return ans

def _028():
	ans = None
	return ans

def _029():
	ans = None
	return ans

def _030():
	ans = None
	return ans

def _031():
	ans = None
	return ans

def _032():
	ans = None
	return ans

def _033():
	ans = None
	return ans

def _034():
	ans = None
	return ans

def _035():
	ans = None
	return ans

def _036():
	ans = None
	return ans

def _037():
	ans = None
	return ans

def _038():
	ans = None
	return ans

def _039():
	ans = None
	return ans

def _040():
	ans = None
	return ans

def _041():
	ans = None
	return ans

def _042():
	ans = None
	return ans

def _043():
	ans = None
	return ans

def _044():
	ans = None
	return ans

def _045():
	ans = None
	return ans

def _046():
	ans = None
	return ans

def _047():
	ans = None
	return ans

def _048():
	ans = None
	return ans

def _049():
	ans = None
	return ans

def _050():
	ans = None
	return ans

def _051():
	ans = None
	return ans

def _052():
	ans = None
	return ans

def _053():
	ans = None
	return ans

def _054():
	ans = None
	return ans

def _055():
	ans = None
	return ans

def _056():
	ans = None
	return ans

def _057():
	ans = None
	return ans

def _058():
	ans = None
	return ans

def _059():
	ans = None
	return ans

def _060():
	ans = None
	return ans

def _061():
	ans = None
	return ans

def _062():
	ans = None
	return ans

def _063():
	ans = None
	return ans

def _064():
	ans = None
	return ans

def _065():
	ans = None
	return ans

def _066():
	ans = None
	return ans

def _067():
	ans = None
	return ans

def _068():
	ans = None
	return ans

def _069():
	ans = None
	return ans

def _070():
	ans = None
	return ans

def _071():
	ans = None
	return ans

def _072():
	ans = None
	return ans

def _073():
	ans = None
	return ans

def _074():
	ans = None
	return ans

def _075():
	ans = None
	return ans

def _076():
	ans = None
	return ans

def _077():
	ans = None
	return ans

def _078():
	ans = None
	return ans

def _079():
	ans = None
	return ans

def _080():
	ans = None
	return ans

def _081():
	ans = None
	return ans

def _082():
	ans = None
	return ans

def _083():
	ans = None
	return ans

def _084():
	ans = None
	return ans

def _085():
	ans = None
	return ans

def _086():
	ans = None
	return ans

def _087():
	ans = None
	return ans

def _088():
	ans = None
	return ans

def _089():
	ans = None
	return ans

def _090():
	ans = None
	return ans

def _091():
	ans = None
	return ans

def _092():
	ans = None
	return ans

def _093():
	ans = None
	return ans

def _094():
	ans = None
	return ans

def _095():
	ans = None
	return ans

def _096():
	ans = None
	return ans

def _097():
	ans = None
	return ans

def _098():
	ans = None
	return ans

def _099():
	ans = None
	return ans

def _100():
	ans = None
	return ans

def _101():
	ans = None
	return ans

def _102():
	ans = None
	return ans

def _103():
	ans = None
	return ans

def _104():
	ans = None
	return ans

def _105():
	ans = None
	return ans

def _106():
	ans = None
	return ans

def _107():
	ans = None
	return ans

def _108():
	ans = None
	return ans

def _109():
	ans = None
	return ans

def _110():
	ans = None
	return ans

def _111():
	ans = None
	return ans

def _112():
	ans = None
	return ans

def _113():
	ans = None
	return ans

def _114():
	ans = None
	return ans

def _115():
	ans = None
	return ans

def _116():
	ans = None
	return ans

def _117():
	ans = None
	return ans

def _118():
	ans = None
	return ans

def _119():
	ans = None
	return ans

def _120():
	ans = None
	return ans

def _121():
	ans = None
	return ans

def _122():
	ans = None
	return ans

def _123():
	ans = None
	return ans

def _124():
	ans = None
	return ans

def _125():
	ans = None
	return ans

def _126():
	ans = None
	return ans

def _127():
	ans = None
	return ans

def _128():
	ans = None
	return ans

def _129():
	ans = None
	return ans

def _130():
	ans = None
	return ans

def _131():
	ans = None
	return ans

def _132():
	ans = None
	return ans

def _133():
	ans = None
	return ans

def _134():
	ans = None
	return ans

def _135():
	ans = None
	return ans

def _136():
	ans = None
	return ans

def _137():
	ans = None
	return ans

def _138():
	ans = None
	return ans

def _139():
	ans = None
	return ans

def _140():
	ans = None
	return ans

def _141():
	ans = None
	return ans

def _142():
	ans = None
	return ans

def _143():
	ans = None
	return ans

def _144():
	ans = None
	return ans

def _145():
	ans = None
	return ans

def _146():
	ans = None
	return ans

def _147():
	ans = None
	return ans

def _148():
	ans = None
	return ans

def _149():
	ans = None
	return ans

def _150():
	ans = None
	return ans

def _151():
	ans = None
	return ans

def _152():
	ans = None
	return ans

def _153():
	ans = None
	return ans

def _154():
	ans = None
	return ans

def _155():
	ans = None
	return ans

def _156():
	ans = None
	return ans

def _157():
	ans = None
	return ans

def _158():
	ans = None
	return ans

def _159():
	ans = None
	return ans

def _160():
	ans = None
	return ans

def _161():
	ans = None
	return ans

def _162():
	ans = None
	return ans

def _163():
	ans = None
	return ans

def _164():
	ans = None
	return ans

def _165():
	ans = None
	return ans

def _166():
	ans = None
	return ans

def _167():
	ans = None
	return ans

def _168():
	ans = None
	return ans

def _169():
	ans = None
	return ans

def _170():
	ans = None
	return ans

def _171():
	ans = None
	return ans

def _172():
	ans = None
	return ans

def _173():
	ans = None
	return ans

def _174():
	ans = None
	return ans

def _175():
	ans = None
	return ans

def _176():
	ans = None
	return ans

def _177():
	ans = None
	return ans

def _178():
	ans = None
	return ans

def _179():
	ans = None
	return ans

def _180():
	ans = None
	return ans

def _181():
	ans = None
	return ans

def _182():
	ans = None
	return ans

def _183():
	ans = None
	return ans

def _184():
	ans = None
	return ans

def _185():
	ans = None
	return ans

def _186():
	ans = None
	return ans

def _187():
	ans = None
	return ans

def _188():
	ans = None
	return ans

def _189():
	ans = None
	return ans

def _190():
	ans = None
	return ans

def _191():
	ans = None
	return ans

def _192():
	ans = None
	return ans

def _193():
	ans = None
	return ans

def _194():
	ans = None
	return ans

def _195():
	ans = None
	return ans

def _196():
	ans = None
	return ans

def _197():
	ans = None
	return ans

def _198():
	ans = None
	return ans

def _199():
	ans = None
	return ans

def _200():
	ans = None
	return ans

def _201():
	ans = None
	return ans

def _202():
	ans = None
	return ans

def _203():
	ans = None
	return ans

def _204():
	ans = None
	return ans

def _205():
	ans = None
	return ans

def _206():
	ans = None
	return ans

def _207():
	ans = None
	return ans

def _208():
	ans = None
	return ans

def _209():
	ans = None
	return ans

def _210():
	ans = None
	return ans

def _211():
	ans = None
	return ans

def _212():
	ans = None
	return ans

def _213():
	ans = None
	return ans

def _214():
	ans = None
	return ans

def _215():
	ans = None
	return ans

def _216():
	ans = None
	return ans

def _217():
	ans = None
	return ans

def _218():
	ans = None
	return ans

def _219():
	ans = None
	return ans

def _220():
	ans = None
	return ans

def _221():
	ans = None
	return ans

def _222():
	ans = None
	return ans

def _223():
	ans = None
	return ans

def _224():
	ans = None
	return ans

def _225():
	ans = None
	return ans

def _226():
	ans = None
	return ans

def _227():
	ans = None
	return ans

def _228():
	ans = None
	return ans

def _229():
	ans = None
	return ans

def _230():
	ans = None
	return ans

def _231():
	ans = None
	return ans

def _232():
	ans = None
	return ans

def _233():
	ans = None
	return ans

def _234():
	ans = None
	return ans

def _235():
	ans = None
	return ans

def _236():
	ans = None
	return ans

def _237():
	ans = None
	return ans

def _238():
	ans = None
	return ans

def _239():
	ans = None
	return ans

def _240():
	ans = None
	return ans

def _241():
	ans = None
	return ans

def _242():
	ans = None
	return ans

def _243():
	ans = None
	return ans

def _244():
	ans = None
	return ans

def _245():
	ans = None
	return ans

def _246():
	ans = None
	return ans

def _247():
	ans = None
	return ans

def _248():
	ans = None
	return ans

def _249():
	ans = None
	return ans

def _250():
	ans = None
	return ans

def _251():
	ans = None
	return ans

def _252():
	ans = None
	return ans

def _253():
	ans = None
	return ans

def _254():
	ans = None
	return ans

def _255():
	ans = None
	return ans

def _256():
	ans = None
	return ans

def _257():
	ans = None
	return ans

def _258():
	ans = None
	return ans

def _259():
	ans = None
	return ans

def _260():
	ans = None
	return ans

def _261():
	ans = None
	return ans

def _262():
	ans = None
	return ans

def _263():
	ans = None
	return ans

def _264():
	ans = None
	return ans

def _265():
	ans = None
	return ans

def _266():
	ans = None
	return ans

def _267():
	ans = None
	return ans

def _268():
	ans = None
	return ans

def _269():
	ans = None
	return ans

def _270():
	ans = None
	return ans

def _271():
	ans = None
	return ans

def _272():
	ans = None
	return ans

def _273():
	ans = None
	return ans

def _274():
	ans = None
	return ans

def _275():
	ans = None
	return ans

def _276():
	ans = None
	return ans

def _277():
	ans = None
	return ans

def _278():
	ans = None
	return ans

def _279():
	ans = None
	return ans

def _280():
	ans = None
	return ans

def _281():
	ans = None
	return ans

def _282():
	ans = None
	return ans

def _283():
	ans = None
	return ans

def _284():
	ans = None
	return ans

def _285():
	ans = None
	return ans

def _286():
	ans = None
	return ans

def _287():
	ans = None
	return ans

def _288():
	ans = None
	return ans

def _289():
	ans = None
	return ans

def _290():
	ans = None
	return ans

def _291():
	ans = None
	return ans

def _292():
	ans = None
	return ans

def _293():
	ans = None
	return ans

def _294():
	ans = None
	return ans

def _295():
	ans = None
	return ans

def _296():
	ans = None
	return ans

def _297():
	ans = None
	return ans

def _298():
	ans = None
	return ans

def _299():
	ans = None
	return ans

def _300():
	ans = None
	return ans

def _301():
	ans = None
	return ans

def _302():
	ans = None
	return ans

def _303():
	ans = None
	return ans

def _304():
	ans = None
	return ans

def _305():
	ans = None
	return ans

def _306():
	ans = None
	return ans

def _307():
	ans = None
	return ans

def _308():
	ans = None
	return ans

def _309():
	ans = None
	return ans

def _310():
	ans = None
	return ans

def _311():
	ans = None
	return ans

def _312():
	ans = None
	return ans

def _313():
	ans = None
	return ans

def _314():
	ans = None
	return ans

def _315():
	ans = None
	return ans

def _316():
	ans = None
	return ans

def _317():
	ans = None
	return ans

def _318():
	ans = None
	return ans

def _319():
	ans = None
	return ans

def _320():
	ans = None
	return ans

def _321():
	ans = None
	return ans

def _322():
	ans = None
	return ans

def _323():
	ans = None
	return ans

def _324():
	ans = None
	return ans

def _325():
	ans = None
	return ans

def _326():
	ans = None
	return ans

def _327():
	ans = None
	return ans

def _328():
	ans = None
	return ans

def _329():
	ans = None
	return ans

def _330():
	ans = None
	return ans

def _331():
	ans = None
	return ans

def _332():
	ans = None
	return ans

def _333():
	ans = None
	return ans

def _334():
	ans = None
	return ans

def _335():
	ans = None
	return ans

def _336():
	ans = None
	return ans

def _337():
	ans = None
	return ans

def _338():
	ans = None
	return ans

def _339():
	ans = None
	return ans

def _340():
	ans = None
	return ans

def _341():
	ans = None
	return ans

def _342():
	ans = None
	return ans

def _343():
	ans = None
	return ans

def _344():
	ans = None
	return ans

def _345():
	ans = None
	return ans

def _346():
	ans = None
	return ans

def _347():
	ans = None
	return ans

def _348():
	ans = None
	return ans

def _349():
	ans = None
	return ans

def _350():
	ans = None
	return ans

def _351():
	ans = None
	return ans

def _352():
	ans = None
	return ans

def _353():
	ans = None
	return ans

def _354():
	ans = None
	return ans

def _355():
	ans = None
	return ans

def _356():
	ans = None
	return ans

def _357():
	ans = None
	return ans

def _358():
	ans = None
	return ans

def _359():
	ans = None
	return ans

def _360():
	ans = None
	return ans

def _361():
	ans = None
	return ans

def _362():
	ans = None
	return ans

def _363():
	ans = None
	return ans

def _364():
	ans = None
	return ans

def _365():
	ans = None
	return ans

def _366():
	ans = None
	return ans

def _367():
	ans = None
	return ans

def _368():
	ans = None
	return ans

def _369():
	ans = None
	return ans

def _370():
	ans = None
	return ans

def _371():
	ans = None
	return ans

def _372():
	ans = None
	return ans

def _373():
	ans = None
	return ans

def _374():
	ans = None
	return ans

def _375():
	ans = None
	return ans

def _376():
	ans = None
	return ans

def _377():
	ans = None
	return ans

def _378():
	ans = None
	return ans

def _379():
	ans = None
	return ans

def _380():
	ans = None
	return ans

def _381():
	ans = None
	return ans

def _382():
	ans = None
	return ans

def _383():
	ans = None
	return ans

def _384():
	ans = None
	return ans

def _385():
	ans = None
	return ans

def _386():
	ans = None
	return ans

def _387():
	ans = None
	return ans

def _388():
	ans = None
	return ans

def _389():
	ans = None
	return ans

def _390():
	ans = None
	return ans

def _391():
	ans = None
	return ans

def _392():
	ans = None
	return ans

def _393():
	ans = None
	return ans

def _394():
	ans = None
	return ans

def _395():
	ans = None
	return ans

def _396():
	ans = None
	return ans

def _397():
	ans = None
	return ans

def _398():
	ans = None
	return ans

def _399():
	ans = None
	return ans

def _400():
	ans = None
	return ans

def _401():
	ans = None
	return ans

def _402():
	ans = None
	return ans

def _403():
	ans = None
	return ans

def _404():
	ans = None
	return ans

def _405():
	ans = None
	return ans

def _406():
	ans = None
	return ans

def _407():
	ans = None
	return ans

def _408():
	ans = None
	return ans

def _409():
	ans = None
	return ans

def _410():
	ans = None
	return ans

def _411():
	ans = None
	return ans

def _412():
	ans = None
	return ans

def _413():
	ans = None
	return ans

def _414():
	ans = None
	return ans

def _415():
	ans = None
	return ans

def _416():
	ans = None
	return ans

def _417():
	ans = None
	return ans

def _418():
	ans = None
	return ans

def _419():
	ans = None
	return ans

def _420():
	ans = None
	return ans

def _421():
	ans = None
	return ans

def _422():
	ans = None
	return ans

def _423():
	ans = None
	return ans

def _424():
	ans = None
	return ans

def _425():
	ans = None
	return ans

def _426():
	ans = None
	return ans

def _427():
	ans = None
	return ans

def _428():
	ans = None
	return ans

def _429():
	ans = None
	return ans

def _430():
	ans = None
	return ans

def _431():
	ans = None
	return ans

def _432():
	ans = None
	return ans

def _433():
	ans = None
	return ans

def _434():
	ans = None
	return ans

def _435():
	ans = None
	return ans

def _436():
	ans = None
	return ans

def _437():
	ans = None
	return ans

def _438():
	ans = None
	return ans

def _439():
	ans = None
	return ans

def _440():
	ans = None
	return ans

def _441():
	ans = None
	return ans

def _442():
	ans = None
	return ans

def _443():
	ans = None
	return ans

def _444():
	ans = None
	return ans

def _445():
	ans = None
	return ans

def _446():
	ans = None
	return ans

def _447():
	ans = None
	return ans

def _448():
	ans = None
	return ans

def _449():
	ans = None
	return ans

def _450():
	ans = None
	return ans

def _451():
	ans = None
	return ans

def _452():
	ans = None
	return ans

def _453():
	ans = None
	return ans

def _454():
	ans = None
	return ans

def _455():
	ans = None
	return ans

def _456():
	ans = None
	return ans

def _457():
	ans = None
	return ans

def _458():
	ans = None
	return ans

def _459():
	ans = None
	return ans

def _460():
	ans = None
	return ans

def _461():
	ans = None
	return ans

def _462():
	ans = None
	return ans

def _463():
	ans = None
	return ans

def _464():
	ans = None
	return ans

def _465():
	ans = None
	return ans

def _466():
	ans = None
	return ans

def _467():
	ans = None
	return ans

def _468():
	ans = None
	return ans

def _469():
	ans = None
	return ans

def _470():
	ans = None
	return ans

def _471():
	ans = None
	return ans

def _472():
	ans = None
	return ans

def _473():
	ans = None
	return ans

def _474():
	ans = None
	return ans

def _475():
	ans = None
	return ans

def _476():
	ans = None
	return ans

def _477():
	ans = None
	return ans

def _478():
	ans = None
	return ans

def _479():
	ans = None
	return ans

def _480():
	ans = None
	return ans

def _481():
	ans = None
	return ans

def _482():
	ans = None
	return ans

def _483():
	ans = None
	return ans

def _484():
	ans = None
	return ans

def _485():
	ans = None
	return ans

def _486():
	ans = None
	return ans

def _487():
	ans = None
	return ans

def _488():
	ans = None
	return ans

def _489():
	ans = None
	return ans

def _490():
	ans = None
	return ans

def _491():
	ans = None
	return ans

def _492():
	ans = None
	return ans

def _493():
	ans = None
	return ans

def _494():
	ans = None
	return ans

def _495():
	ans = None
	return ans

def _496():
	ans = None
	return ans

def _497():
	ans = None
	return ans

def _498():
	ans = None
	return ans

def _499():
	ans = None
	return ans

def _500():
	ans = None
	return ans
