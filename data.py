import numpy as np

_ = '''

num_data = 20
x_dim = 5
x_group = 1

a_dim = (num_data, x_dim)
x_dim = (x_dim, x_group)
b_dim = (num_data, x_group)

A = np.random.randn(a_dim[0], a_dim[1]) * 4
x = np.random.randn(x_dim[0], x_dim[1]) * 4
b = A @ x

print(A)
print(b)
print(x)'''

A = np.array([[  2.53767484,   1.80941758,   3.88277187,  -5.34867116,  -7.66774537],
 [ -8.25187074,   6.62151445,  -8.48330938,  -2.7613249 ,   6.28912909],
 [ -0.06696199,  -3.8821875 ,   0.9680242 ,  -5.71364126,   0.32109948],
 [ -1.03075807,   3.22186007,  -2.51175713,   8.31911773,  -3.33944785],
 [  2.21283549,  -0.72010504,   1.28513907,  -6.03776033,  -0.38572879],
 [ -5.07247505,  -0.23048821,   1.59594851,  -6.14179429,   5.30907319],
 [  1.81308316,   4.02933236,  -4.11907264,  -0.85708172, -10.277714  ],
 [  7.29847047,   2.79888142,   1.54468491,   1.68780565,   5.30409654],
 [ -0.40179998,  -8.24175242,   1.88019465,  -1.71630637,  -0.77607085],
 [  4.08948119,   5.17091568,  -3.60534862,  -1.28167845, -10.77769738],
 [  1.90072742,   0.50304634,   0.23985791,   0.96663968,  -4.25965365],
 [ -4.0945924 ,  -3.39049539,   0.69747086,   5.23055254,  -0.10535582],
 [ -0.06225651,   1.61730072,  -1.11302166,   1.28706299,   0.66011601],
 [ -4.60719871,  -1.93767416,   7.76038975,  -0.68684785,   1.99285352],
 [  4.31992497,   4.9985453 ,  -1.82523427,  -3.50382127,  -5.42630208],
 [ -8.37351486,  -4.13463775,   3.225535  ,   1.15077832,  -3.19220004],
 [  3.5623725 ,   0.89689431,   9.39721605,  -3.64954248,  -2.03551311],
 [ -8.10503544,   2.64546464,   3.67163676,  -2.48551769,  -2.69599336],
 [  2.43659564,  -1.34373255,   6.87897348,  -6.194929  ,   3.31951194],
 [ -5.31411989,  -3.68224247,   3.22016275,  -2.26944055,  -6.97391262]])

b = np.array([[-27.23822838],
 [-33.28812963],
 [-14.99393712],
 [ 42.47671663],
 [-31.20596091],
 [-42.36448155],
 [  9.85360059],
 [-25.17831239],
 [ 25.30161819],
 [  1.02570943],
 [ 10.85032225],
 [ 43.39987236],
 [  0.37552044],
 [-12.77984735],
 [-26.23945228],
 [ 31.10305204],
 [-40.55263564],
 [-19.32506665],
 [-50.21523928],
 [ 18.29177345]])

x = np.array([[-0.78049754],
 [-4.35782416],
 [-2.13749351],
 [ 5.09882175],
 [-2.37343103]])