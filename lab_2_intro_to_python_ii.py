# -*- coding: utf-8 -*-
"""Lab 2 - Intro_to_Python_II.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IKYD4P4bOK66bccBzCrNEN21-d88BHoG

# **Lab 2 - Introduction to Python programming II**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab2"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True

"""**Enter your name, section number, and BYU NetID**"""

# Enter your first and last names in between the quotation marks.

first_name="Collin"

last_name="Zoeller"

# Enter your Math 215 section number in between the quotation marks. 

section_number="Your Math 215 section number goes here"  

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER!

BYUNetID="czoeller"

"""**Problem 1**"""

first_elem=1   # Replace the value of 0 with the number described in Problem 1.

"""**Problem 2**"""

def sum_list(L):
  sum = 0
  for i in L:
    sum = sum + i
  return sum

"""**Problem 3**"""

def list_relu(L):
  new_list=L.copy()  # Remember to create a copy of your list.  After this lab you'll need to remember to do it on your own.
  for i in range(len(new_list)):
    if new_list[i] < 0:
      new_list[i] = 0
  return new_list

"""**Problem 4**"""

import numpy as np  # Importing NumPy

my_var=397.24594182538  # Replace the value of 0 with the required value from Problem 4.

"""**Problem 5**"""

my_vect_var= np.array([ 3.45833333,  2.125     , -2.91666667,  2.125     ,  3.45833333])  # Replace the value of 0 with the required value from Problem 5.

"""**Problem 6**"""

def first_rpt(M):
  new_matrix=M.copy() 
  for i in range(len(new_matrix)):
    new_matrix[i]=new_matrix[0]
  return new_matrix

"""**Problem 7**"""

def matrix_sum(M):
  sum = 0
  for i in range(len(M)):
    for j in range(len(M[0,:])):
      sum = sum + M[i,j]
  return sum

"""**Problem 8**"""

long_list= [0.5,
 0.25,
 0.125,
 0.0625,
 0.03125,
 0.015625,
 0.0078125,
 0.00390625,
 0.001953125,
 0.0009765625,
 0.00048828125,
 0.000244140625,
 0.0001220703125,
 6.103515625e-05,
 3.0517578125e-05,
 1.52587890625e-05,
 7.62939453125e-06,
 3.814697265625e-06,
 1.9073486328125e-06,
 9.5367431640625e-07,
 4.76837158203125e-07,
 2.384185791015625e-07,
 1.1920928955078125e-07,
 5.960464477539063e-08,
 2.9802322387695312e-08,
 1.4901161193847656e-08,
 7.450580596923828e-09,
 3.725290298461914e-09,
 1.862645149230957e-09,
 9.313225746154785e-10,
 4.656612873077393e-10,
 2.3283064365386963e-10,
 1.1641532182693481e-10,
 5.820766091346741e-11,
 2.9103830456733704e-11,
 1.4551915228366852e-11,
 7.275957614183426e-12,
 3.637978807091713e-12,
 1.8189894035458565e-12,
 9.094947017729282e-13,
 4.547473508864641e-13,
 2.2737367544323206e-13,
 1.1368683772161603e-13,
 5.684341886080802e-14,
 2.842170943040401e-14,
 1.4210854715202004e-14,
 7.105427357601002e-15,
 3.552713678800501e-15,
 1.7763568394002505e-15,
 8.881784197001252e-16,
 4.440892098500626e-16,
 2.220446049250313e-16,
 1.1102230246251565e-16,
 5.551115123125783e-17,
 2.7755575615628914e-17,
 1.3877787807814457e-17,
 6.938893903907228e-18,
 3.469446951953614e-18,
 1.734723475976807e-18,
 8.673617379884035e-19,
 4.336808689942018e-19,
 2.168404344971009e-19,
 1.0842021724855044e-19,
 5.421010862427522e-20,
 2.710505431213761e-20,
 1.3552527156068805e-20,
 6.776263578034403e-21,
 3.3881317890172014e-21,
 1.6940658945086007e-21,
 8.470329472543003e-22,
 4.235164736271502e-22,
 2.117582368135751e-22,
 1.0587911840678754e-22,
 5.293955920339377e-23,
 2.6469779601696886e-23,
 1.3234889800848443e-23,
 6.617444900424222e-24,
 3.308722450212111e-24,
 1.6543612251060553e-24,
 8.271806125530277e-25,
 4.1359030627651384e-25,
 2.0679515313825692e-25,
 1.0339757656912846e-25,
 5.169878828456423e-26,
 2.5849394142282115e-26,
 1.2924697071141057e-26,
 6.462348535570529e-27,
 3.2311742677852644e-27,
 1.6155871338926322e-27,
 8.077935669463161e-28,
 4.0389678347315804e-28,
 2.0194839173657902e-28,
 1.0097419586828951e-28,
 5.048709793414476e-29,
 2.524354896707238e-29,
 1.262177448353619e-29,
 6.310887241768095e-30,
 3.1554436208840472e-30,
 1.5777218104420236e-30,
 7.888609052210118e-31]  # Replace the value of 0 with the required list from Problem 8.

"""**Problem 9**"""

very_long_list= [1,
 2,
 3,
 1,
 4,
 9,
 1,
 8,
 27,
 1,
 16,
 81,
 1,
 32,
 243,
 1,
 64,
 729,
 1,
 128,
 2187,
 1,
 256,
 6561,
 1,
 512,
 19683,
 1,
 1024,
 59049,
 1,
 2048,
 177147,
 1,
 4096,
 531441,
 1,
 8192,
 1594323,
 1,
 16384,
 4782969,
 1,
 32768,
 14348907,
 1,
 65536,
 43046721,
 1,
 131072,
 129140163,
 1,
 262144,
 387420489,
 1,
 524288,
 1162261467,
 1,
 1048576,
 3486784401,
 1,
 2097152,
 10460353203,
 1,
 4194304,
 31381059609,
 1,
 8388608,
 94143178827,
 1,
 16777216,
 282429536481,
 1,
 33554432,
 847288609443,
 1,
 67108864,
 2541865828329,
 1,
 134217728,
 7625597484987,
 1,
 268435456,
 22876792454961,
 1,
 536870912,
 68630377364883,
 1,
 1073741824,
 205891132094649,
 1,
 2147483648,
 617673396283947,
 1,
 4294967296,
 1853020188851841,
 1,
 8589934592,
 5559060566555523,
 1,
 17179869184,
 16677181699666569,
 1,
 34359738368,
 50031545098999707,
 1,
 68719476736,
 150094635296999121,
 1,
 137438953472,
 450283905890997363,
 1,
 274877906944,
 1350851717672992089,
 1,
 549755813888,
 4052555153018976267,
 1,
 1099511627776,
 12157665459056928801,
 1,
 2199023255552,
 36472996377170786403,
 1,
 4398046511104,
 109418989131512359209,
 1,
 8796093022208,
 328256967394537077627,
 1,
 17592186044416,
 984770902183611232881,
 1,
 35184372088832,
 2954312706550833698643,
 1,
 70368744177664,
 8862938119652501095929,
 1,
 140737488355328,
 26588814358957503287787,
 1,
 281474976710656,
 79766443076872509863361,
 1,
 562949953421312,
 239299329230617529590083,
 1,
 1125899906842624,
 717897987691852588770249,
 1,
 2251799813685248,
 2153693963075557766310747,
 1,
 4503599627370496,
 6461081889226673298932241,
 1,
 9007199254740992,
 19383245667680019896796723,
 1,
 18014398509481984,
 58149737003040059690390169,
 1,
 36028797018963968,
 174449211009120179071170507,
 1,
 72057594037927936,
 523347633027360537213511521,
 1,
 144115188075855872,
 1570042899082081611640534563,
 1,
 288230376151711744,
 4710128697246244834921603689,
 1,
 576460752303423488,
 14130386091738734504764811067,
 1,
 1152921504606846976,
 42391158275216203514294433201,
 1,
 2305843009213693952,
 127173474825648610542883299603,
 1,
 4611686018427387904,
 381520424476945831628649898809,
 1,
 9223372036854775808,
 1144561273430837494885949696427,
 1,
 18446744073709551616,
 3433683820292512484657849089281,
 1,
 36893488147419103232,
 10301051460877537453973547267843,
 1,
 73786976294838206464,
 30903154382632612361920641803529,
 1,
 147573952589676412928,
 92709463147897837085761925410587,
 1,
 295147905179352825856,
 278128389443693511257285776231761,
 1,
 590295810358705651712,
 834385168331080533771857328695283,
 1,
 1180591620717411303424,
 2503155504993241601315571986085849,
 1,
 2361183241434822606848,
 7509466514979724803946715958257547,
 1,
 4722366482869645213696,
 22528399544939174411840147874772641,
 1,
 9444732965739290427392,
 67585198634817523235520443624317923,
 1,
 18889465931478580854784,
 202755595904452569706561330872953769,
 1,
 37778931862957161709568,
 608266787713357709119683992618861307,
 1,
 75557863725914323419136,
 1824800363140073127359051977856583921,
 1,
 151115727451828646838272,
 5474401089420219382077155933569751763,
 1,
 302231454903657293676544,
 16423203268260658146231467800709255289,
 1,
 604462909807314587353088,
 49269609804781974438694403402127765867,
 1,
 1208925819614629174706176,
 147808829414345923316083210206383297601,
 1,
 2417851639229258349412352,
 443426488243037769948249630619149892803,
 1,
 4835703278458516698824704,
 1330279464729113309844748891857449678409,
 1,
 9671406556917033397649408,
 3990838394187339929534246675572349035227,
 1,
 19342813113834066795298816,
 11972515182562019788602740026717047105681,
 1,
 38685626227668133590597632,
 35917545547686059365808220080151141317043,
 1,
 77371252455336267181195264,
 107752636643058178097424660240453423951129,
 1,
 154742504910672534362390528,
 323257909929174534292273980721360271853387,
 1,
 309485009821345068724781056,
 969773729787523602876821942164080815560161,
 1,
 618970019642690137449562112,
 2909321189362570808630465826492242446680483,
 1,
 1237940039285380274899124224,
 8727963568087712425891397479476727340041449,
 1,
 2475880078570760549798248448,
 26183890704263137277674192438430182020124347,
 1,
 4951760157141521099596496896,
 78551672112789411833022577315290546060373041,
 1,
 9903520314283042199192993792,
 235655016338368235499067731945871638181119123,
 1,
 19807040628566084398385987584,
 706965049015104706497203195837614914543357369,
 1,
 39614081257132168796771975168,
 2120895147045314119491609587512844743630072107,
 1,
 79228162514264337593543950336,
 6362685441135942358474828762538534230890216321,
 1,
 158456325028528675187087900672,
 19088056323407827075424486287615602692670648963,
 1,
 316912650057057350374175801344,
 57264168970223481226273458862846808078011946889,
 1,
 633825300114114700748351602688,
 171792506910670443678820376588540424234035840667]   # Replace the value of 0 with the required list from Problem 9.

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to http://www.math.byu.edu:30000 for grading.
"""