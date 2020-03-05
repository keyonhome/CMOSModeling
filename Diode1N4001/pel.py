! Program transform to extract IS, N, RS
! from forward diode I-V characteristics
!
! Note: print statements go to the
!       window used to start IC-CAP

print "Example Program Transform to extract DC Diode Parameters"

index = 0             ! array index
!
! pick 2 low current points for IS & N
! to be extracted from
v1 = va[index]        ! 1st voltage step
WHILE v1 < 0.4        ! get first data
  index = index + 1   !  point pair
  v1 = va[index]
END WHILE
i1 = ia[index]

v2 = va[index]        ! get second data
WHILE v2 < 0.5        !  point pair
  index = index + 1
  v2 = va[index]
END WHILE
i2 = ia[index]

! extraction equations for IS & N
vt = 8.62e-5 * (TNOM + 273.15)
N = 1 / vt * (v2-v1) / log(i2 / i1)
IS = sqrt(i1 * i2) / exp((v1+v2)/(2*N*vt))

! get high current data point for RS
! to be extracted from
WHILE va[index] < 0.8
  index = index + 1
END WHILE

! extraction equations for RS
idmax = IS * exp(va[index] / N / vt)
                     ! max ideal current
idreal = ia[index]   ! actual current
vjcn = N * vt * log(idreal / IS)
                     ! junction voltage
RS = (va[index] - vjcn) / idreal

print "IS = ";IS;"   N = ";N;"   RS = ";RS
print
print "... end of program transform extraction ..."

