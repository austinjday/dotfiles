# encoding: utf-8
# module scipy.linalg._flapack
# from C:\Users\austi\Anaconda3\lib\site-packages\scipy\linalg\_flapack.cp36-win_amd64.pyd
# by generator 1.145
"""
This module '_flapack' is auto-generated with f2py (version:2).
Functions:
  a,b,alphar,alphai,beta,q,z,m,pl,pr,dif,work,iwork,info = stgsen(select,a,b,q,z,lwork=MAX(4*n+16,2*m*(n-m)),liwork=n+6,overwrite_a=0,overwrite_b=0,overwrite_q=0,overwrite_z=0)
  a,b,alphar,alphai,beta,q,z,m,pl,pr,dif,work,iwork,info = dtgsen(select,a,b,q,z,lwork=MAX(4*n+16,2*m*(n-m)),liwork=n+6,overwrite_a=0,overwrite_b=0,overwrite_q=0,overwrite_z=0)
  a,b,alpha,beta,q,z,m,pl,pr,dif,work,iwork,info = ctgsen(select,a,b,q,z,lwork=2*m*(n-m),liwork=n+2,overwrite_a=0,overwrite_b=0,overwrite_q=0,overwrite_z=0)
  a,b,alpha,beta,q,z,m,pl,pr,dif,work,iwork,info = ztgsen(select,a,b,q,z,lwork=2*m*(n-m),liwork=n+2,overwrite_a=0,overwrite_b=0,overwrite_q=0,overwrite_z=0)
  a,b,sdim,alphar,alphai,beta,vsl,vsr,work,info = sgges(sselect,a,b,jobvsl=1,jobvsr=1,sort_t=0,ldvsl=((jobvsl==1)?n:1),ldvsr=((jobvsr==1)?n:1),lwork=8*n+16,sselect_extra_args=(),overwrite_a=0,overwrite_b=0)
  a,b,sdim,alphar,alphai,beta,vsl,vsr,work,info = dgges(dselect,a,b,jobvsl=1,jobvsr=1,sort_t=0,ldvsl=((jobvsl==1)?n:1),ldvsr=((jobvsr==1)?n:1),lwork=8*n+16,dselect_extra_args=(),overwrite_a=0,overwrite_b=0)
  a,b,sdim,alpha,beta,vsl,vsr,work,info = cgges(cselect,a,b,jobvsl=1,jobvsr=1,sort_t=0,ldvsl=((jobvsl==1)?n:1),ldvsr=((jobvsr==1)?n:1),lwork=2*n,cselect_extra_args=(),overwrite_a=0,overwrite_b=0)
  a,b,sdim,alpha,beta,vsl,vsr,work,info = zgges(zselect,a,b,jobvsl=1,jobvsr=1,sort_t=0,ldvsl=((jobvsl==1)?n:1),ldvsr=((jobvsr==1)?n:1),lwork=2*n,zselect_extra_args=(),overwrite_a=0,overwrite_b=0)
  c,info = spbtrf(ab,lower=0,ldab=shape(ab,0),overwrite_ab=0)
  c,info = dpbtrf(ab,lower=0,ldab=shape(ab,0),overwrite_ab=0)
  c,info = cpbtrf(ab,lower=0,ldab=shape(ab,0),overwrite_ab=0)
  c,info = zpbtrf(ab,lower=0,ldab=shape(ab,0),overwrite_ab=0)
  x,info = spbtrs(ab,b,lower=0,ldab=shape(ab,0),overwrite_b=0)
  x,info = dpbtrs(ab,b,lower=0,ldab=shape(ab,0),overwrite_b=0)
  x,info = cpbtrs(ab,b,lower=0,ldab=shape(ab,0),overwrite_b=0)
  x,info = zpbtrs(ab,b,lower=0,ldab=shape(ab,0),overwrite_b=0)
  x,info = strtrs(a,b,lower=0,trans=0,unitdiag=0,lda=shape(a,0),overwrite_b=0)
  x,info = dtrtrs(a,b,lower=0,trans=0,unitdiag=0,lda=shape(a,0),overwrite_b=0)
  x,info = ctrtrs(a,b,lower=0,trans=0,unitdiag=0,lda=shape(a,0),overwrite_b=0)
  x,info = ztrtrs(a,b,lower=0,trans=0,unitdiag=0,lda=shape(a,0),overwrite_b=0)
  c,x,info = spbsv(ab,b,lower=0,ldab=shape(ab,0),overwrite_ab=0,overwrite_b=0)
  c,x,info = dpbsv(ab,b,lower=0,ldab=shape(ab,0),overwrite_ab=0,overwrite_b=0)
  c,x,info = cpbsv(ab,b,lower=0,ldab=shape(ab,0),overwrite_ab=0,overwrite_b=0)
  c,x,info = zpbsv(ab,b,lower=0,ldab=shape(ab,0),overwrite_ab=0,overwrite_b=0)
  d,du,x,info = sptsv(d,e,b,overwrite_d=0,overwrite_e=0,overwrite_b=0)
  d,du,x,info = dptsv(d,e,b,overwrite_d=0,overwrite_e=0,overwrite_b=0)
  d,du,x,info = cptsv(d,e,b,overwrite_d=0,overwrite_e=0,overwrite_b=0)
  d,du,x,info = zptsv(d,e,b,overwrite_d=0,overwrite_e=0,overwrite_b=0)
  ba,lo,hi,pivscale,info = sgebal(a,scale=0,permute=0,overwrite_a=0)
  ba,lo,hi,pivscale,info = dgebal(a,scale=0,permute=0,overwrite_a=0)
  ba,lo,hi,pivscale,info = cgebal(a,scale=0,permute=0,overwrite_a=0)
  ba,lo,hi,pivscale,info = zgebal(a,scale=0,permute=0,overwrite_a=0)
  ht,tau,info = sgehrd(a,lo=0,hi=n-1,lwork=MAX(n,1),overwrite_a=0)
  ht,tau,info = dgehrd(a,lo=0,hi=n-1,lwork=MAX(n,1),overwrite_a=0)
  ht,tau,info = cgehrd(a,lo=0,hi=n-1,lwork=MAX(n,1),overwrite_a=0)
  ht,tau,info = zgehrd(a,lo=0,hi=n-1,lwork=MAX(n,1),overwrite_a=0)
  work,info = sgehrd_lwork(n,lo=0,hi=n-1)
  work,info = dgehrd_lwork(n,lo=0,hi=n-1)
  work,info = cgehrd_lwork(n,lo=0,hi=n-1)
  work,info = zgehrd_lwork(n,lo=0,hi=n-1)
  ht,info = sorghr(a,tau,lo=0,hi=n-1,lwork=hi-lo,overwrite_a=0)
  ht,info = dorghr(a,tau,lo=0,hi=n-1,lwork=hi-lo,overwrite_a=0)
  work,info = sorghr_lwork(n,lo=0,hi=n-1)
  work,info = dorghr_lwork(n,lo=0,hi=n-1)
  ht,info = cunghr(a,tau,lo=0,hi=n-1,lwork=hi-lo,overwrite_a=0)
  ht,info = zunghr(a,tau,lo=0,hi=n-1,lwork=hi-lo,overwrite_a=0)
  work,info = cunghr_lwork(n,lo=0,hi=n-1)
  work,info = zunghr_lwork(n,lo=0,hi=n-1)
  lub,piv,x,info = sgbsv(kl,ku,ab,b,overwrite_ab=0,overwrite_b=0)
  lub,piv,x,info = dgbsv(kl,ku,ab,b,overwrite_ab=0,overwrite_b=0)
  lub,piv,x,info = cgbsv(kl,ku,ab,b,overwrite_ab=0,overwrite_b=0)
  lub,piv,x,info = zgbsv(kl,ku,ab,b,overwrite_ab=0,overwrite_b=0)
  du2,d,du,x,info = sgtsv(dl,d,du,b,overwrite_dl=0,overwrite_d=0,overwrite_du=0,overwrite_b=0)
  du2,d,du,x,info = dgtsv(dl,d,du,b,overwrite_dl=0,overwrite_d=0,overwrite_du=0,overwrite_b=0)
  du2,d,du,x,info = cgtsv(dl,d,du,b,overwrite_dl=0,overwrite_d=0,overwrite_du=0,overwrite_b=0)
  du2,d,du,x,info = zgtsv(dl,d,du,b,overwrite_dl=0,overwrite_d=0,overwrite_du=0,overwrite_b=0)
  lu,piv,x,info = sgesv(a,b,overwrite_a=0,overwrite_b=0)
  lu,piv,x,info = dgesv(a,b,overwrite_a=0,overwrite_b=0)
  lu,piv,x,info = cgesv(a,b,overwrite_a=0,overwrite_b=0)
  lu,piv,x,info = zgesv(a,b,overwrite_a=0,overwrite_b=0)
  lu,piv,info = sgetrf(a,overwrite_a=0)
  lu,piv,info = dgetrf(a,overwrite_a=0)
  lu,piv,info = cgetrf(a,overwrite_a=0)
  lu,piv,info = zgetrf(a,overwrite_a=0)
  x,info = sgetrs(lu,piv,b,trans=0,overwrite_b=0)
  x,info = dgetrs(lu,piv,b,trans=0,overwrite_b=0)
  x,info = cgetrs(lu,piv,b,trans=0,overwrite_b=0)
  x,info = zgetrs(lu,piv,b,trans=0,overwrite_b=0)
  inv_a,info = sgetri(lu,piv,lwork=3*n,overwrite_lu=0)
  inv_a,info = dgetri(lu,piv,lwork=3*n,overwrite_lu=0)
  inv_a,info = cgetri(lu,piv,lwork=3*n,overwrite_lu=0)
  inv_a,info = zgetri(lu,piv,lwork=3*n,overwrite_lu=0)
  work,info = sgetri_lwork(n)
  work,info = dgetri_lwork(n)
  work,info = cgetri_lwork(n)
  work,info = zgetri_lwork(n)
  u,s,vt,info = sgesdd(a,compute_uv=1,full_matrices=1,lwork=(compute_uv?4*minmn*minmn+MAX(m,n)+9*minmn:MAX(14*minmn+4,10*minmn+2+25*(25+8))+MAX(m,n)),overwrite_a=0)
  u,s,vt,info = dgesdd(a,compute_uv=1,full_matrices=1,lwork=(compute_uv?4*minmn*minmn+MAX(m,n)+9*minmn:MAX(14*minmn+4,10*minmn+2+25*(25+8))+MAX(m,n)),overwrite_a=0)
  work,info = sgesdd_lwork(m,n,compute_uv=1,full_matrices=1)
  work,info = dgesdd_lwork(m,n,compute_uv=1,full_matrices=1)
  u,s,vt,info = cgesdd(a,compute_uv=1,full_matrices=1,lwork=(compute_uv?2*minmn*minmn+MAX(m,n)+2*minmn:2*minmn+MAX(m,n)),overwrite_a=0)
  u,s,vt,info = zgesdd(a,compute_uv=1,full_matrices=1,lwork=(compute_uv?2*minmn*minmn+MAX(m,n)+2*minmn:2*minmn+MAX(m,n)),overwrite_a=0)
  work,info = cgesdd_lwork(m,n,compute_uv=1,full_matrices=1)
  work,info = zgesdd_lwork(m,n,compute_uv=1,full_matrices=1)
  u,s,vt,info = sgesvd(a,compute_uv=1,full_matrices=1,lwork=MAX(1,MAX(3*minmn+MAX(m,n),5*minmn)),overwrite_a=0)
  u,s,vt,info = dgesvd(a,compute_uv=1,full_matrices=1,lwork=MAX(1,MAX(3*minmn+MAX(m,n),5*minmn)),overwrite_a=0)
  work,info = sgesvd_lwork(m,n,compute_uv=1,full_matrices=1)
  work,info = dgesvd_lwork(m,n,compute_uv=1,full_matrices=1)
  u,s,vt,info = cgesvd(a,compute_uv=1,full_matrices=1,lwork=MAX(1,2*minmn+MAX(m,n)),overwrite_a=0)
  u,s,vt,info = zgesvd(a,compute_uv=1,full_matrices=1,lwork=MAX(1,2*minmn+MAX(m,n)),overwrite_a=0)
  work,info = cgesvd_lwork(m,n,compute_uv=1,full_matrices=1)
  work,info = zgesvd_lwork(m,n,compute_uv=1,full_matrices=1)
  v,x,s,rank,work,info = sgelss(a,b,cond=-1.0,lwork=3*minmn+MAX(2*minmn,MAX(maxmn,nrhs)),overwrite_a=0,overwrite_b=0)
  v,x,s,rank,work,info = dgelss(a,b,cond=-1.0,lwork=3*minmn+MAX(2*minmn,MAX(maxmn,nrhs)),overwrite_a=0,overwrite_b=0)
  work,info = sgelss_lwork(m,n,nrhs,cond=-1.0,lwork=-1)
  work,info = dgelss_lwork(m,n,nrhs,cond=-1.0,lwork=-1)
  v,x,s,rank,work,info = cgelss(a,b,cond=-1.0,lwork=2*minmn+MAX(maxmn,nrhs),overwrite_a=0,overwrite_b=0)
  v,x,s,rank,work,info = zgelss(a,b,cond=-1.0,lwork=2*minmn+MAX(maxmn,nrhs),overwrite_a=0,overwrite_b=0)
  delta,sigma,work,info = slasd4(i,d,z,rho=1.0)
  delta,sigma,work,info = dlasd4(i,d,z,rho=1.0)
  work,info = cgelss_lwork(m,n,nrhs,cond=-1.0,lwork=-1)
  work,info = zgelss_lwork(m,n,nrhs,cond=-1.0,lwork=-1)
  v,x,j,rank,info = sgelsy(a,b,jptv,cond,lwork,overwrite_a=0,overwrite_b=0)
  v,x,j,rank,info = dgelsy(a,b,jptv,cond,lwork,overwrite_a=0,overwrite_b=0)
  work,info = sgelsy_lwork(m,n,nrhs,cond,lwork=-1)
  work,info = dgelsy_lwork(m,n,nrhs,cond,lwork=-1)
  v,x,j,rank,info = cgelsy(a,b,jptv,cond,lwork,overwrite_a=0,overwrite_b=0)
  v,x,j,rank,info = zgelsy(a,b,jptv,cond,lwork,overwrite_a=0,overwrite_b=0)
  work,info = cgelsy_lwork(m,n,nrhs,cond,lwork=-1)
  work,info = zgelsy_lwork(m,n,nrhs,cond,lwork=-1)
  x,s,rank,info = sgelsd(a,b,lwork,size_iwork,cond=-1.0,overwrite_a=0,overwrite_b=0)
  x,s,rank,info = dgelsd(a,b,lwork,size_iwork,cond=-1.0,overwrite_a=0,overwrite_b=0)
  work,iwork,info = sgelsd_lwork(m,n,nrhs,cond=-1.0,lwork=-1)
  work,iwork,info = dgelsd_lwork(m,n,nrhs,cond=-1.0,lwork=-1)
  x,s,rank,info = cgelsd(a,b,lwork,size_rwork,size_iwork,cond=-1.0,overwrite_a=0,overwrite_b=0)
  x,s,rank,info = zgelsd(a,b,lwork,size_rwork,size_iwork,cond=-1.0,overwrite_a=0,overwrite_b=0)
  work,rwork,iwork,info = cgelsd_lwork(m,n,nrhs,cond=-1.0,lwork=-1)
  work,rwork,iwork,info = zgelsd_lwork(m,n,nrhs,cond=-1.0,lwork=-1)
  qr,jpvt,tau,work,info = sgeqp3(a,lwork=3*(n+1),overwrite_a=0)
  qr,jpvt,tau,work,info = dgeqp3(a,lwork=3*(n+1),overwrite_a=0)
  qr,jpvt,tau,work,info = cgeqp3(a,lwork=3*(n+1),overwrite_a=0)
  qr,jpvt,tau,work,info = zgeqp3(a,lwork=3*(n+1),overwrite_a=0)
  qr,tau,work,info = sgeqrf(a,lwork=3*n,overwrite_a=0)
  qr,tau,work,info = dgeqrf(a,lwork=3*n,overwrite_a=0)
  qr,tau,work,info = cgeqrf(a,lwork=3*n,overwrite_a=0)
  qr,tau,work,info = zgeqrf(a,lwork=3*n,overwrite_a=0)
  qr,tau,work,info = sgerqf(a,lwork=3*m,overwrite_a=0)
  qr,tau,work,info = dgerqf(a,lwork=3*m,overwrite_a=0)
  qr,tau,work,info = cgerqf(a,lwork=3*m,overwrite_a=0)
  qr,tau,work,info = zgerqf(a,lwork=3*m,overwrite_a=0)
  q,work,info = sorgqr(a,tau,lwork=3*n,overwrite_a=0)
  q,work,info = dorgqr(a,tau,lwork=3*n,overwrite_a=0)
  q,work,info = cungqr(a,tau,lwork=3*n,overwrite_a=0)
  q,work,info = zungqr(a,tau,lwork=3*n,overwrite_a=0)
  cq,work,info = sormqr(side,trans,a,tau,c,lwork,overwrite_c=0)
  cq,work,info = dormqr(side,trans,a,tau,c,lwork,overwrite_c=0)
  cq,work,info = cunmqr(side,trans,a,tau,c,lwork,overwrite_c=0)
  cq,work,info = zunmqr(side,trans,a,tau,c,lwork,overwrite_c=0)
  q,work,info = sorgrq(a,tau,lwork=3*m,overwrite_a=0)
  q,work,info = dorgrq(a,tau,lwork=3*m,overwrite_a=0)
  q,work,info = cungrq(a,tau,lwork=3*m,overwrite_a=0)
  q,work,info = zungrq(a,tau,lwork=3*m,overwrite_a=0)
  wr,wi,vl,vr,info = sgeev(a,compute_vl=1,compute_vr=1,lwork=4*n,overwrite_a=0)
  wr,wi,vl,vr,info = dgeev(a,compute_vl=1,compute_vr=1,lwork=4*n,overwrite_a=0)
  work,info = sgeev_lwork(n,compute_vl=1,compute_vr=1)
  work,info = dgeev_lwork(n,compute_vl=1,compute_vr=1)
  w,vl,vr,info = cgeev(a,compute_vl=1,compute_vr=1,lwork=2*n,overwrite_a=0)
  w,vl,vr,info = zgeev(a,compute_vl=1,compute_vr=1,lwork=2*n,overwrite_a=0)
  work,info = cgeev_lwork(n,compute_vl=1,compute_vr=1)
  work,info = zgeev_lwork(n,compute_vl=1,compute_vr=1)
  alphar,alphai,beta,vl,vr,info = sgegv(a,b,compute_vl=1,compute_vr=1,lwork=8*n,overwrite_a=0,overwrite_b=0)
  alphar,alphai,beta,vl,vr,info = dgegv(a,b,compute_vl=1,compute_vr=1,lwork=8*n,overwrite_a=0,overwrite_b=0)
  alpha,beta,vl,vr,info = cgegv(a,b,compute_vl=1,compute_vr=1,lwork=2*n,overwrite_a=0,overwrite_b=0)
  alpha,beta,vl,vr,info = zgegv(a,b,compute_vl=1,compute_vr=1,lwork=2*n,overwrite_a=0,overwrite_b=0)
  w,v,info = ssyev(a,compute_v=1,lower=0,lwork=3*n-1,overwrite_a=0)
  w,v,info = dsyev(a,compute_v=1,lower=0,lwork=3*n-1,overwrite_a=0)
  w,v,info = cheev(a,compute_v=1,lower=0,lwork=2*n-1,overwrite_a=0)
  w,v,info = zheev(a,compute_v=1,lower=0,lwork=2*n-1,overwrite_a=0)
  w,v,info = ssyevd(a,compute_v=1,lower=0,lwork=(compute_v?1+6*n+2*n*n:2*n+1),overwrite_a=0)
  w,v,info = dsyevd(a,compute_v=1,lower=0,lwork=(compute_v?1+6*n+2*n*n:2*n+1),overwrite_a=0)
  w,v,info = cheevd(a,compute_v=1,lower=0,lwork=(compute_v?2*n+n*n:n+1),overwrite_a=0)
  w,v,info = zheevd(a,compute_v=1,lower=0,lwork=(compute_v?2*n+n*n:n+1),overwrite_a=0)
  c,x,info = sposv(a,b,lower=0,overwrite_a=0,overwrite_b=0)
  c,x,info = dposv(a,b,lower=0,overwrite_a=0,overwrite_b=0)
  c,x,info = cposv(a,b,lower=0,overwrite_a=0,overwrite_b=0)
  c,x,info = zposv(a,b,lower=0,overwrite_a=0,overwrite_b=0)
  c,info = spotrf(a,lower=0,clean=1,overwrite_a=0)
  c,info = dpotrf(a,lower=0,clean=1,overwrite_a=0)
  c,info = cpotrf(a,lower=0,clean=1,overwrite_a=0)
  c,info = zpotrf(a,lower=0,clean=1,overwrite_a=0)
  x,info = spotrs(c,b,lower=0,overwrite_b=0)
  x,info = dpotrs(c,b,lower=0,overwrite_b=0)
  x,info = cpotrs(c,b,lower=0,overwrite_b=0)
  x,info = zpotrs(c,b,lower=0,overwrite_b=0)
  inv_a,info = spotri(c,lower=0,overwrite_c=0)
  inv_a,info = dpotri(c,lower=0,overwrite_c=0)
  inv_a,info = cpotri(c,lower=0,overwrite_c=0)
  inv_a,info = zpotri(c,lower=0,overwrite_c=0)
  a,info = slauum(c,lower=0,overwrite_c=0)
  a,info = dlauum(c,lower=0,overwrite_c=0)
  a,info = clauum(c,lower=0,overwrite_c=0)
  a,info = zlauum(c,lower=0,overwrite_c=0)
  inv_c,info = strtri(c,lower=0,unitdiag=0,overwrite_c=0)
  inv_c,info = dtrtri(c,lower=0,unitdiag=0,overwrite_c=0)
  inv_c,info = ctrtri(c,lower=0,unitdiag=0,overwrite_c=0)
  inv_c,info = ztrtri(c,lower=0,unitdiag=0,overwrite_c=0)
  x,scale,info = strsyl(a,b,c,trana='N',tranb='N',isgn=1,overwrite_c=0)
  x,scale,info = dtrsyl(a,b,c,trana='N',tranb='N',isgn=1,overwrite_c=0)
  x,scale,info = ctrsyl(a,b,c,trana='N',tranb='N',isgn=1,overwrite_c=0)
  x,scale,info = ztrsyl(a,b,c,trana='N',tranb='N',isgn=1,overwrite_c=0)
  a = slaswp(a,piv,k1=0,k2=len(piv)-1,off=0,inc=1,overwrite_a=0)
  a = dlaswp(a,piv,k1=0,k2=len(piv)-1,off=0,inc=1,overwrite_a=0)
  a = claswp(a,piv,k1=0,k2=len(piv)-1,off=0,inc=1,overwrite_a=0)
  a = zlaswp(a,piv,k1=0,k2=len(piv)-1,off=0,inc=1,overwrite_a=0)
  t,sdim,w,vs,work,info = cgees(cselect,a,compute_v=1,sort_t=0,lwork=3*n,cselect_extra_args=(),overwrite_a=0)
  t,sdim,w,vs,work,info = zgees(zselect,a,compute_v=1,sort_t=0,lwork=3*n,zselect_extra_args=(),overwrite_a=0)
  t,sdim,wr,wi,vs,work,info = sgees(sselect,a,compute_v=1,sort_t=0,lwork=3*n,sselect_extra_args=(),overwrite_a=0)
  t,sdim,wr,wi,vs,work,info = dgees(dselect,a,compute_v=1,sort_t=0,lwork=3*n,dselect_extra_args=(),overwrite_a=0)
  alphar,alphai,beta,vl,vr,work,info = sggev(a,b,compute_vl=1,compute_vr=1,lwork=8*n,overwrite_a=0,overwrite_b=0)
  alphar,alphai,beta,vl,vr,work,info = dggev(a,b,compute_vl=1,compute_vr=1,lwork=8*n,overwrite_a=0,overwrite_b=0)
  alpha,beta,vl,vr,work,info = cggev(a,b,compute_vl=1,compute_vr=1,lwork=2*n,overwrite_a=0,overwrite_b=0)
  alpha,beta,vl,vr,work,info = zggev(a,b,compute_vl=1,compute_vr=1,lwork=2*n,overwrite_a=0,overwrite_b=0)
  w,z,info = ssbev(ab,compute_v=1,lower=0,ldab=shape(ab,0),overwrite_ab=1)
  w,z,info = dsbev(ab,compute_v=1,lower=0,ldab=shape(ab,0),overwrite_ab=1)
  w,z,info = ssbevd(ab,compute_v=1,lower=0,ldab=shape(ab,0),liwork=(compute_v?3+5*n:1),overwrite_ab=1)
  w,z,info = dsbevd(ab,compute_v=1,lower=0,ldab=shape(ab,0),liwork=(compute_v?3+5*n:1),overwrite_ab=1)
  w,z,m,ifail,info = ssbevx(ab,vl,vu,il,iu,ldab=shape(ab,0),compute_v=1,range=0,lower=0,abstol=0.0,mmax=(compute_v?(range==2?(iu-il+1):n):1),overwrite_ab=1)
  w,z,m,ifail,info = dsbevx(ab,vl,vu,il,iu,ldab=shape(ab,0),compute_v=1,range=0,lower=0,abstol=0.0,mmax=(compute_v?(range==2?(iu-il+1):n):1),overwrite_ab=1)
  w,z,info = chbevd(ab,compute_v=1,lower=0,ldab=shape(ab,0),lrwork=(compute_v?1+5*n+2*n*n:n),liwork=(compute_v?3+5*n:1),overwrite_ab=1)
  w,z,info = zhbevd(ab,compute_v=1,lower=0,ldab=shape(ab,0),lrwork=(compute_v?1+5*n+2*n*n:n),liwork=(compute_v?3+5*n:1),overwrite_ab=1)
  w,z,m,ifail,info = chbevx(ab,vl,vu,il,iu,ldab=shape(ab,0),compute_v=1,range=0,lower=0,abstol=0.0,mmax=(compute_v?(range==2?(iu-il+1):n):1),overwrite_ab=1)
  w,z,m,ifail,info = zhbevx(ab,vl,vu,il,iu,ldab=shape(ab,0),compute_v=1,range=0,lower=0,abstol=0.0,mmax=(compute_v?(range==2?(iu-il+1):n):1),overwrite_ab=1)
  dlamch = dlamch(cmach)
  slamch = slamch(cmach)
  lu,ipiv,info = sgbtrf(ab,kl,ku,m=shape(ab,1),n=shape(ab,1),ldab=shape(ab,0),overwrite_ab=0)
  lu,ipiv,info = dgbtrf(ab,kl,ku,m=shape(ab,1),n=shape(ab,1),ldab=shape(ab,0),overwrite_ab=0)
  lu,ipiv,info = cgbtrf(ab,kl,ku,m=shape(ab,1),n=shape(ab,1),ldab=shape(ab,0),overwrite_ab=0)
  lu,ipiv,info = zgbtrf(ab,kl,ku,m=shape(ab,1),n=shape(ab,1),ldab=shape(ab,0),overwrite_ab=0)
  x,info = sgbtrs(ab,kl,ku,b,ipiv,trans=0,n=shape(ab,1),ldab=shape(ab,0),ldb=shape(b,0),overwrite_b=0)
  x,info = dgbtrs(ab,kl,ku,b,ipiv,trans=0,n=shape(ab,1),ldab=shape(ab,0),ldb=shape(b,0),overwrite_b=0)
  x,info = cgbtrs(ab,kl,ku,b,ipiv,trans=0,n=shape(ab,1),ldab=shape(ab,0),ldb=shape(b,0),overwrite_b=0)
  x,info = zgbtrs(ab,kl,ku,b,ipiv,trans=0,n=shape(ab,1),ldab=shape(ab,0),ldb=shape(b,0),overwrite_b=0)
  w,z,info = ssyevr(a,jobz='V',range='A',uplo='L',il=1,iu=n,lwork=26*n,overwrite_a=0)
  w,z,info = dsyevr(a,jobz='V',range='A',uplo='L',il=1,iu=n,lwork=26*n,overwrite_a=0)
  w,z,info = cheevr(a,jobz='V',range='A',uplo='L',il=1,iu=n,lwork=18*n,overwrite_a=0)
  w,z,info = zheevr(a,jobz='V',range='A',uplo='L',il=1,iu=n,lwork=18*n,overwrite_a=0)
  a,w,info = ssygv(a,b,itype=1,jobz='V',uplo='L',overwrite_a=0,overwrite_b=0)
  a,w,info = dsygv(a,b,itype=1,jobz='V',uplo='L',overwrite_a=0,overwrite_b=0)
  a,w,info = chegv(a,b,itype=1,jobz='V',uplo='L',overwrite_a=0,overwrite_b=0)
  a,w,info = zhegv(a,b,itype=1,jobz='V',uplo='L',overwrite_a=0,overwrite_b=0)
  a,w,info = ssygvd(a,b,itype=1,jobz='V',uplo='L',lwork=1+6*n+2*n*n,overwrite_a=0,overwrite_b=0)
  a,w,info = dsygvd(a,b,itype=1,jobz='V',uplo='L',lwork=1+6*n+2*n*n,overwrite_a=0,overwrite_b=0)
  a,w,info = chegvd(a,b,itype=1,jobz='V',uplo='L',lwork=2*n+n*n,overwrite_a=0,overwrite_b=0)
  a,w,info = zhegvd(a,b,itype=1,jobz='V',uplo='L',lwork=2*n+n*n,overwrite_a=0,overwrite_b=0)
  w,z,ifail,info = ssygvx(a,b,iu,itype=1,jobz='V',uplo='L',il=1,lwork=8*n,overwrite_a=0,overwrite_b=0)
  w,z,ifail,info = dsygvx(a,b,iu,itype=1,jobz='V',uplo='L',il=1,lwork=8*n,overwrite_a=0,overwrite_b=0)
  w,z,ifail,info = chegvx(a,b,iu,itype=1,jobz='V',uplo='L',il=1,lwork=18*n-1,overwrite_a=0,overwrite_b=0)
  w,z,ifail,info = zhegvx(a,b,iu,itype=1,jobz='V',uplo='L',il=1,lwork=18*n-1,overwrite_a=0,overwrite_b=0)
  n2 = slange(norm,a)
  n2 = dlange(norm,a)
  n2 = clange(norm,a)
  n2 = zlange(norm,a)
  alpha,x,tau = slarfg(n,alpha,x,incx=1,overwrite_x=0)
  alpha,x,tau = dlarfg(n,alpha,x,incx=1,overwrite_x=0)
  alpha,x,tau = clarfg(n,alpha,x,incx=1,overwrite_x=0)
  alpha,x,tau = zlarfg(n,alpha,x,incx=1,overwrite_x=0)
  c = slarf(v,tau,c,work,side='L',incv=1,overwrite_c=0)
  c = dlarf(v,tau,c,work,side='L',incv=1,overwrite_c=0)
  c = clarf(v,tau,c,work,side='L',incv=1,overwrite_c=0)
  c = zlarf(v,tau,c,work,side='L',incv=1,overwrite_c=0)
  cs,sn,r = slartg(f,g)
  cs,sn,r = dlartg(f,g)
  cs,sn,r = clartg(f,g)
  cs,sn,r = zlartg(f,g)
  x,y = crot(x,y,c,s,n=(len(x)-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)
  x,y = zrot(x,y,c,s,n=(len(x)-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)
  major,minor,patch = ilaver()
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def cgbsv(kl, ku, ab, b, overwrite_ab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lub,piv,x,info = cgbsv(kl,ku,ab,b,[overwrite_ab,overwrite_b])
    
    Wrapper for ``cgbsv``.
    
    Parameters
    ----------
    kl : input int
    ku : input int
    ab : input rank-2 array('F') with bounds (2*kl+ku+1,n)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    lub : rank-2 array('F') with bounds (2*kl+ku+1,n) and ab storage
    piv : rank-1 array('i') with bounds (n)
    x : rank-2 array('F') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def cgbtrf(ab, kl, ku, m=None, n=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    lu,ipiv,info = cgbtrf(ab,kl,ku,[m,n,ldab,overwrite_ab])
    
    Wrapper for ``cgbtrf``.
    
    Parameters
    ----------
    ab : input rank-2 array('F') with bounds (ldab,*)
    kl : input int
    ku : input int
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(ab,1)
    n : input int, optional
        Default: shape(ab,1)
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    
    Returns
    -------
    lu : rank-2 array('F') with bounds (ldab,*) and ab storage
    ipiv : rank-1 array('i') with bounds (MIN(m,n))
    info : int
    """
    pass

def cgbtrs(ab, kl, ku, b, ipiv, trans=None, n=None, ldab=None, ldb=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = cgbtrs(ab,kl,ku,b,ipiv,[trans,n,ldab,ldb,overwrite_b])
    
    Wrapper for ``cgbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('F') with bounds (ldab,*)
    kl : input int
    ku : input int
    b : input rank-2 array('F') with bounds (ldb,*)
    ipiv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    n : input int, optional
        Default: shape(ab,1)
    ldab : input int, optional
        Default: shape(ab,0)
    ldb : input int, optional
        Default: shape(b,0)
    
    Returns
    -------
    x : rank-2 array('F') with bounds (ldb,*) and b storage
    info : int
    """
    pass

def cgebal(a, scale=None, permute=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ba,lo,hi,pivscale,info = cgebal(a,[scale,permute,overwrite_a])
    
    Wrapper for ``cgebal``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    scale : input int, optional
        Default: 0
    permute : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    ba : rank-2 array('F') with bounds (m,n) and a storage
    lo : int
    hi : int
    pivscale : rank-1 array('f') with bounds (n)
    info : int
    """
    pass

def cgees(cselect, a, compute_v=None, sort_t=None, lwork=None, cselect_extra_args=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    t,sdim,w,vs,work,info = cgees(cselect,a,[compute_v,sort_t,lwork,cselect_extra_args,overwrite_a])
    
    Wrapper for ``cgees``.
    
    Parameters
    ----------
    cselect : call-back function
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    sort_t : input int, optional
        Default: 0
    cselect_extra_args : input tuple, optional
        Default: ()
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n
    
    Returns
    -------
    t : rank-2 array('F') with bounds (n,n) and a storage
    sdim : int
    w : rank-1 array('F') with bounds (n)
    vs : rank-2 array('F') with bounds (ldvs,n)
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def cselect(arg): return cselect
      Required arguments:
        arg : input complex
      Return objects:
        cselect : int
    """
    pass

def cgeev(a, compute_vl=None, compute_vr=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,vl,vr,info = cgeev(a,[compute_vl,compute_vr,lwork,overwrite_a])
    
    Wrapper for ``cgeev``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 2*n
    
    Returns
    -------
    w : rank-1 array('F') with bounds (n)
    vl : rank-2 array('F') with bounds (ldvl,n)
    vr : rank-2 array('F') with bounds (ldvr,n)
    info : int
    """
    pass

def cgeev_lwork(n, compute_vl=None, compute_vr=None): # real signature unknown; restored from __doc__
    """
    work,info = cgeev_lwork(n,[compute_vl,compute_vr])
    
    Wrapper for ``cgeev_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgegv(*args, **kwds): # reliably restored by inspect
    """
    `cgegv` is deprecated!
    The `*gegv` family of routines has been deprecated in
    LAPACK 3.6.0 in favor of the `*ggev` family of routines.
    The corresponding wrappers will be removed from SciPy in
    a future release.
    
    alpha,beta,vl,vr,info = cgegv(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``cgegv``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 2*n
    
    Returns
    -------
    alpha : rank-1 array('F') with bounds (n)
    beta : rank-1 array('F') with bounds (n)
    vl : rank-2 array('F') with bounds (ldvl,n)
    vr : rank-2 array('F') with bounds (ldvr,n)
    info : int
    """
    pass

def cgehrd(a, lo=None, hi=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ht,tau,info = cgehrd(a,[lo,hi,lwork,overwrite_a])
    
    Wrapper for ``cgehrd``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(n,1)
    
    Returns
    -------
    ht : rank-2 array('F') with bounds (n,n) and a storage
    tau : rank-1 array('F') with bounds (n - 1)
    info : int
    """
    pass

def cgehrd_lwork(n, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    work,info = cgehrd_lwork(n,[lo,hi])
    
    Wrapper for ``cgehrd_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgelsd(a, b, lwork, size_rwork, size_iwork, cond=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,s,rank,info = cgelsd(a,b,lwork,size_rwork,size_iwork,[cond,overwrite_a,overwrite_b])
    
    Wrapper for ``cgelsd``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    b : input rank-2 array('F') with bounds (maxmn,nrhs)
    lwork : input int
    size_rwork : input int
    size_iwork : input int
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    cond : input float, optional
        Default: -1.0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (maxmn,nrhs) and b storage
    s : rank-1 array('f') with bounds (minmn)
    rank : int
    info : int
    """
    pass

def cgelsd_lwork(m, n, nrhs, cond=None, lwork=None): # real signature unknown; restored from __doc__
    """
    work,rwork,iwork,info = cgelsd_lwork(m,n,nrhs,[cond,lwork])
    
    Wrapper for ``cgelsd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : complex
    rwork : float
    iwork : int
    info : int
    """
    pass

def cgelss(a, b, cond=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    v,x,s,rank,work,info = cgelss(a,b,[cond,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``cgelss``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    b : input rank-2 array('F') with bounds (maxmn,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: 2*minmn+MAX(maxmn,nrhs)
    
    Returns
    -------
    v : rank-2 array('F') with bounds (m,n) and a storage
    x : rank-2 array('F') with bounds (maxmn,nrhs) and b storage
    s : rank-1 array('f') with bounds (minmn)
    rank : int
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def cgelss_lwork(m, n, nrhs, cond=None, lwork=None): # real signature unknown; restored from __doc__
    """
    work,info = cgelss_lwork(m,n,nrhs,[cond,lwork])
    
    Wrapper for ``cgelss_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgelsy(a, b, jptv, cond, lwork, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    v,x,j,rank,info = cgelsy(a,b,jptv,cond,lwork,[overwrite_a,overwrite_b])
    
    Wrapper for ``cgelsy``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    b : input rank-2 array('F') with bounds (maxmn,nrhs)
    jptv : input rank-1 array('i') with bounds (n)
    cond : input float
    lwork : input int
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    v : rank-2 array('F') with bounds (m,n) and a storage
    x : rank-2 array('F') with bounds (maxmn,nrhs) and b storage
    j : rank-1 array('i') with bounds (n) and jptv storage
    rank : int
    info : int
    """
    pass

def cgelsy_lwork(m, n, nrhs, cond, lwork=None): # real signature unknown; restored from __doc__
    """
    work,info = cgelsy_lwork(m,n,nrhs,cond,[lwork])
    
    Wrapper for ``cgelsy_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    cond : input float
    
    Other Parameters
    ----------------
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgeqp3(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,jpvt,tau,work,info = cgeqp3(a,[lwork,overwrite_a])
    
    Wrapper for ``cgeqp3``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*(n+1)
    
    Returns
    -------
    qr : rank-2 array('F') with bounds (m,n) and a storage
    jpvt : rank-1 array('i') with bounds (n)
    tau : rank-1 array('F') with bounds (MIN(m,n))
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def cgeqrf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,work,info = cgeqrf(a,[lwork,overwrite_a])
    
    Wrapper for ``cgeqrf``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n
    
    Returns
    -------
    qr : rank-2 array('F') with bounds (m,n) and a storage
    tau : rank-1 array('F') with bounds (MIN(m,n))
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def cgerqf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,work,info = cgerqf(a,[lwork,overwrite_a])
    
    Wrapper for ``cgerqf``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*m
    
    Returns
    -------
    qr : rank-2 array('F') with bounds (m,n) and a storage
    tau : rank-1 array('F') with bounds (MIN(m,n))
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def cgesdd(a, compute_uv=None, full_matrices=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    u,s,vt,info = cgesdd(a,[compute_uv,full_matrices,lwork,overwrite_a])
    
    Wrapper for ``cgesdd``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    lwork : input int, optional
        Default: (compute_uv?2*minmn*minmn+MAX(m,n)+2*minmn:2*minmn+MAX(m,n))
    
    Returns
    -------
    u : rank-2 array('F') with bounds (u0,u1)
    s : rank-1 array('f') with bounds (minmn)
    vt : rank-2 array('F') with bounds (vt0,vt1)
    info : int
    """
    pass

def cgesdd_lwork(m, n, compute_uv=None, full_matrices=None): # real signature unknown; restored from __doc__
    """
    work,info = cgesdd_lwork(m,n,[compute_uv,full_matrices])
    
    Wrapper for ``cgesdd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgesv(a, b, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lu,piv,x,info = cgesv(a,b,[overwrite_a,overwrite_b])
    
    Wrapper for ``cgesv``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('F') with bounds (n,n) and a storage
    piv : rank-1 array('i') with bounds (n)
    x : rank-2 array('F') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def cgesvd(a, compute_uv=None, full_matrices=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    u,s,vt,info = cgesvd(a,[compute_uv,full_matrices,lwork,overwrite_a])
    
    Wrapper for ``cgesvd``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    lwork : input int, optional
        Default: MAX(1,2*minmn+MAX(m,n))
    
    Returns
    -------
    u : rank-2 array('F') with bounds (u0,u1)
    s : rank-1 array('f') with bounds (minmn)
    vt : rank-2 array('F') with bounds (vt0,vt1)
    info : int
    """
    pass

def cgesvd_lwork(m, n, compute_uv=None, full_matrices=None): # real signature unknown; restored from __doc__
    """
    work,info = cgesvd_lwork(m,n,[compute_uv,full_matrices])
    
    Wrapper for ``cgesvd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgetrf(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    lu,piv,info = cgetrf(a,[overwrite_a])
    
    Wrapper for ``cgetrf``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('F') with bounds (m,n) and a storage
    piv : rank-1 array('i') with bounds (MIN(m,n))
    info : int
    """
    pass

def cgetri(lu, piv, lwork=None, overwrite_lu=None): # real signature unknown; restored from __doc__
    """
    inv_a,info = cgetri(lu,piv,[lwork,overwrite_lu])
    
    Wrapper for ``cgetri``.
    
    Parameters
    ----------
    lu : input rank-2 array('F') with bounds (n,n)
    piv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_lu : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n
    
    Returns
    -------
    inv_a : rank-2 array('F') with bounds (n,n) and lu storage
    info : int
    """
    pass

def cgetri_lwork(n): # real signature unknown; restored from __doc__
    """
    work,info = cgetri_lwork(n)
    
    Wrapper for ``cgetri_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgetrs(lu, piv, b, trans=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = cgetrs(lu,piv,b,[trans,overwrite_b])
    
    Wrapper for ``cgetrs``.
    
    Parameters
    ----------
    lu : input rank-2 array('F') with bounds (n,n)
    piv : input rank-1 array('i') with bounds (n)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def cgges(cselect, a, b, jobvsl=None, jobvsr=None, sort_t=None, ldvsl=None, ldvsr=None, lwork=None, cselect_extra_args=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,b,sdim,alpha,beta,vsl,vsr,work,info = cgges(cselect,a,b,[jobvsl,jobvsr,sort_t,ldvsl,ldvsr,lwork,cselect_extra_args,overwrite_a,overwrite_b])
    
    Wrapper for ``cgges``.
    
    Parameters
    ----------
    cselect : call-back function
    a : input rank-2 array('F') with bounds (lda,*)
    b : input rank-2 array('F') with bounds (ldb,*)
    
    Other Parameters
    ----------------
    jobvsl : input int, optional
        Default: 1
    jobvsr : input int, optional
        Default: 1
    sort_t : input int, optional
        Default: 0
    cselect_extra_args : input tuple, optional
        Default: ()
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    ldvsl : input int, optional
        Default: ((jobvsl==1)?n:1)
    ldvsr : input int, optional
        Default: ((jobvsr==1)?n:1)
    lwork : input int, optional
        Default: 2*n
    
    Returns
    -------
    a : rank-2 array('F') with bounds (lda,*)
    b : rank-2 array('F') with bounds (ldb,*)
    sdim : int
    alpha : rank-1 array('F') with bounds (n)
    beta : rank-1 array('F') with bounds (n)
    vsl : rank-2 array('F') with bounds (ldvsl,n)
    vsr : rank-2 array('F') with bounds (ldvsr,n)
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def cselect(alpha,beta): return cselect
      Required arguments:
        alpha : input complex
        beta : input complex
      Return objects:
        cselect : int
    """
    pass

def cggev(a, b, compute_vl=None, compute_vr=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    alpha,beta,vl,vr,work,info = cggev(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``cggev``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 2*n
    
    Returns
    -------
    alpha : rank-1 array('F') with bounds (n)
    beta : rank-1 array('F') with bounds (n)
    vl : rank-2 array('F') with bounds (ldvl,n)
    vr : rank-2 array('F') with bounds (ldvr,n)
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def cgtsv(dl, d, du, b, overwrite_dl=None, overwrite_d=None, overwrite_du=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    du2,d,du,x,info = cgtsv(dl,d,du,b,[overwrite_dl,overwrite_d,overwrite_du,overwrite_b])
    
    Wrapper for ``cgtsv``.
    
    Parameters
    ----------
    dl : input rank-1 array('F') with bounds (n - 1)
    d : input rank-1 array('F') with bounds (*)
    du : input rank-1 array('F') with bounds (n - 1)
    b : input rank-2 array('F') with bounds (*,*)
    
    Other Parameters
    ----------------
    overwrite_dl : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    overwrite_du : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    du2 : rank-1 array('F') with bounds (n - 1) and dl storage
    d : rank-1 array('F') with bounds (*)
    du : rank-1 array('F') with bounds (n - 1)
    x : rank-2 array('F') with bounds (*,*) and b storage
    info : int
    """
    pass

def chbevd(ab, compute_v=None, lower=None, ldab=None, lrwork=None, liwork=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,info = chbevd(ab,[compute_v,lower,ldab,lrwork,liwork,overwrite_ab])
    
    Wrapper for ``chbevd``.
    
    Parameters
    ----------
    ab : input rank-2 array('F') with bounds (ldab,*)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    lrwork : input int, optional
        Default: (compute_v?1+5*n+2*n*n:n)
    liwork : input int, optional
        Default: (compute_v?3+5*n:1)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    z : rank-2 array('F') with bounds (ldz,ldz)
    info : int
    """
    pass

def chbevx(ab, vl, vu, il, iu, ldab=None, compute_v=None, range=None, lower=None, abstol=None, mmax=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,m,ifail,info = chbevx(ab,vl,vu,il,iu,[ldab,compute_v,range,lower,abstol,mmax,overwrite_ab])
    
    Wrapper for ``chbevx``.
    
    Parameters
    ----------
    ab : input rank-2 array('F') with bounds (ldab,*)
    vl : input float
    vu : input float
    il : input int
    iu : input int
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    ldab : input int, optional
        Default: shape(ab,0)
    compute_v : input int, optional
        Default: 1
    range : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    abstol : input float, optional
        Default: 0.0
    mmax : input int, optional
        Default: (compute_v?(range==2?(iu-il+1):n):1)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    z : rank-2 array('F') with bounds (ldz,mmax)
    m : int
    ifail : rank-1 array('i') with bounds ((compute_v?n:1))
    info : int
    """
    pass

def cheev(a, compute_v=None, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,v,info = cheev(a,[compute_v,lower,lwork,overwrite_a])
    
    Wrapper for ``cheev``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 2*n-1
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    v : rank-2 array('F') with bounds (n,n) and a storage
    info : int
    """
    pass

def cheevd(a, compute_v=None, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,v,info = cheevd(a,[compute_v,lower,lwork,overwrite_a])
    
    Wrapper for ``cheevd``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: (compute_v?2*n+n*n:n+1)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    v : rank-2 array('F') with bounds (n,n) and a storage
    info : int
    """
    pass

def cheevr(a, jobz=None, range=None, uplo=None, il=None, iu=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,z,info = cheevr(a,[jobz,range,uplo,il,iu,lwork,overwrite_a])
    
    Wrapper for ``cheevr``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    jobz : input string(len=1), optional
        Default: 'V'
    range : input string(len=1), optional
        Default: 'A'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    il : input int, optional
        Default: 1
    iu : input int, optional
        Default: n
    lwork : input int, optional
        Default: 18*n
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    z : rank-2 array('F') with bounds (n,m)
    info : int
    """
    pass

def chegv(a, b, itype=None, jobz=None, uplo=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,w,info = chegv(a,b,[itype,jobz,uplo,overwrite_a,overwrite_b])
    
    Wrapper for ``chegv``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (n,n)
    w : rank-1 array('f') with bounds (n)
    info : int
    """
    pass

def chegvd(a, b, itype=None, jobz=None, uplo=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,w,info = chegvd(a,b,[itype,jobz,uplo,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``chegvd``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 2*n+n*n
    
    Returns
    -------
    a : rank-2 array('F') with bounds (n,n)
    w : rank-1 array('f') with bounds (n)
    info : int
    """
    pass

def chegvx(a, b, iu, itype=None, jobz=None, uplo=None, il=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    w,z,ifail,info = chegvx(a,b,iu,[itype,jobz,uplo,il,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``chegvx``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,n)
    iu : input int
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    il : input int, optional
        Default: 1
    lwork : input int, optional
        Default: 18*n-1
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    z : rank-2 array('F') with bounds (n,m)
    ifail : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def clange(norm, a): # real signature unknown; restored from __doc__
    """
    n2 = clange(norm,a)
    
    Wrapper for ``clange``.
    
    Parameters
    ----------
    norm : input string(len=1)
    a : input rank-2 array('F') with bounds (m,n)
    
    Returns
    -------
    n2 : float
    """
    pass

def clarf(v, tau, c, work, side=None, incv=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = clarf(v,tau,c,work,[side,incv,overwrite_c])
    
    Wrapper for ``clarf``.
    
    Parameters
    ----------
    v : input rank-1 array('F') with bounds (*)
    tau : input complex
    c : input rank-2 array('F') with bounds (m,n)
    work : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    incv : input int, optional
        Default: 1
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (m,n)
    """
    pass

def clarfg(n, alpha, x, incx=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    alpha,x,tau = clarfg(n,alpha,x,[incx,overwrite_x])
    
    Wrapper for ``clarfg``.
    
    Parameters
    ----------
    n : input int
    alpha : input complex
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    alpha : complex
    x : rank-1 array('F') with bounds (*)
    tau : complex
    """
    pass

def clartg(f, g): # real signature unknown; restored from __doc__
    """
    cs,sn,r = clartg(f,g)
    
    Wrapper for ``clartg``.
    
    Parameters
    ----------
    f : input complex
    g : input complex
    
    Returns
    -------
    cs : float
    sn : complex
    r : complex
    """
    pass

def claswp(a, piv, k1=None, k2=None, off=None, inc=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = claswp(a,piv,[k1,k2,off,inc,overwrite_a])
    
    Wrapper for ``claswp``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (nrows,n)
    piv : input rank-1 array('i') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    k1 : input int, optional
        Default: 0
    k2 : input int, optional
        Default: len(piv)-1
    off : input int, optional
        Default: 0
    inc : input int, optional
        Default: 1
    
    Returns
    -------
    a : rank-2 array('F') with bounds (nrows,n)
    """
    pass

def clauum(c, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    a,info = clauum(c,[lower,overwrite_c])
    
    Wrapper for ``clauum``.
    
    Parameters
    ----------
    c : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (n,n) and c storage
    info : int
    """
    pass

def cpbsv(ab, b, lower=None, ldab=None, overwrite_ab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    c,x,info = cpbsv(ab,b,[lower,ldab,overwrite_ab,overwrite_b])
    
    Wrapper for ``cpbsv``.
    
    Parameters
    ----------
    ab : input rank-2 array('F') with bounds (ldab,n)
    b : input rank-2 array('F') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (ldab,n) and ab storage
    x : rank-2 array('F') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def cpbtrf(ab, lower=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    c,info = cpbtrf(ab,[lower,ldab,overwrite_ab])
    
    Wrapper for ``cpbtrf``.
    
    Parameters
    ----------
    ab : input rank-2 array('F') with bounds (ldab,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    
    Returns
    -------
    c : rank-2 array('F') with bounds (ldab,n) and ab storage
    info : int
    """
    pass

def cpbtrs(ab, b, lower=None, ldab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = cpbtrs(ab,b,[lower,ldab,overwrite_b])
    
    Wrapper for ``cpbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('F') with bounds (ldab,n)
    b : input rank-2 array('F') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def cposv(a, b, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    c,x,info = cposv(a,b,[lower,overwrite_a,overwrite_b])
    
    Wrapper for ``cposv``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (n,n) and a storage
    x : rank-2 array('F') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def cpotrf(a, lower=None, clean=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,info = cpotrf(a,[lower,clean,overwrite_a])
    
    Wrapper for ``cpotrf``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    clean : input int, optional
        Default: 1
    
    Returns
    -------
    c : rank-2 array('F') with bounds (n,n) and a storage
    info : int
    """
    pass

def cpotri(c, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    inv_a,info = cpotri(c,[lower,overwrite_c])
    
    Wrapper for ``cpotri``.
    
    Parameters
    ----------
    c : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    inv_a : rank-2 array('F') with bounds (n,n) and c storage
    info : int
    """
    pass

def cpotrs(c, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = cpotrs(c,b,[lower,overwrite_b])
    
    Wrapper for ``cpotrs``.
    
    Parameters
    ----------
    c : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def cptsv(d, e, b, overwrite_d=None, overwrite_e=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    d,du,x,info = cptsv(d,e,b,[overwrite_d,overwrite_e,overwrite_b])
    
    Wrapper for ``cptsv``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (*)
    e : input rank-1 array('F') with bounds (n - 1)
    b : input rank-2 array('F') with bounds (*,*)
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    d : rank-1 array('f') with bounds (*)
    du : rank-1 array('F') with bounds (n - 1) and e storage
    x : rank-2 array('F') with bounds (*,*) and b storage
    info : int
    """
    pass

def crot(x, y, c, s, n=None, offx=None, incx=None, offy=None, incy=None, overwrite_x=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    x,y = crot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])
    
    Wrapper for ``crot``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    y : input rank-1 array('F') with bounds (*)
    c : input float
    s : input complex
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 0
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('F') with bounds (*)
    y : rank-1 array('F') with bounds (*)
    """
    pass

def ctgsen(select, a, b, q, z, lwork=None, liwork=None, overwrite_a=None, overwrite_b=None, overwrite_q=None, overwrite_z=None): # real signature unknown; restored from __doc__
    """
    a,b,alpha,beta,q,z,m,pl,pr,dif,work,iwork,info = ctgsen(select,a,b,q,z,[lwork,liwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])
    
    Wrapper for ``ctgsen``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    a : input rank-2 array('F') with bounds (lda,*)
    b : input rank-2 array('F') with bounds (ldb,*)
    q : input rank-2 array('F') with bounds (ldq,*)
    z : input rank-2 array('F') with bounds (ldz,*)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    overwrite_z : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 2*m*(n-m)
    liwork : input int, optional
        Default: n+2
    
    Returns
    -------
    a : rank-2 array('F') with bounds (lda,*)
    b : rank-2 array('F') with bounds (ldb,*)
    alpha : rank-1 array('F') with bounds (n)
    beta : rank-1 array('F') with bounds (n)
    q : rank-2 array('F') with bounds (ldq,*)
    z : rank-2 array('F') with bounds (ldz,*)
    m : int
    pl : float
    pr : float
    dif : rank-1 array('f') with bounds (2)
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    iwork : rank-1 array('i') with bounds (MAX(1,liwork))
    info : int
    """
    pass

def ctrsyl(a, b, c, trana=None, tranb=None, isgn=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    x,scale,info = ctrsyl(a,b,c,[trana,tranb,isgn,overwrite_c])
    
    Wrapper for ``ctrsyl``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,m)
    b : input rank-2 array('F') with bounds (n,n)
    c : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    trana : input string(len=1), optional
        Default: 'N'
    tranb : input string(len=1), optional
        Default: 'N'
    isgn : input int, optional
        Default: 1
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (m,n) and c storage
    scale : float
    info : int
    """
    pass

def ctrtri(c, lower=None, unitdiag=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    inv_c,info = ctrtri(c,[lower,unitdiag,overwrite_c])
    
    Wrapper for ``ctrtri``.
    
    Parameters
    ----------
    c : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    
    Returns
    -------
    inv_c : rank-2 array('F') with bounds (n,n) and c storage
    info : int
    """
    pass

def ctrtrs(a, b, lower=None, trans=None, unitdiag=None, lda=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = ctrtrs(a,b,[lower,trans,unitdiag,lda,overwrite_b])
    
    Wrapper for ``ctrtrs``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (lda,n)
    b : input rank-2 array('F') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    lda : input int, optional
        Default: shape(a,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def cunghr(a, tau, lo=None, hi=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ht,info = cunghr(a,tau,[lo,hi,lwork,overwrite_a])
    
    Wrapper for ``cunghr``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    tau : input rank-1 array('F') with bounds (n - 1)
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: hi-lo
    
    Returns
    -------
    ht : rank-2 array('F') with bounds (n,n) and a storage
    info : int
    """
    pass

def cunghr_lwork(n, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    work,info = cunghr_lwork(n,[lo,hi])
    
    Wrapper for ``cunghr_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cungqr(a, tau, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    q,work,info = cungqr(a,tau,[lwork,overwrite_a])
    
    Wrapper for ``cungqr``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    tau : input rank-1 array('F') with bounds (k)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n
    
    Returns
    -------
    q : rank-2 array('F') with bounds (m,n) and a storage
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def cungrq(a, tau, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    q,work,info = cungrq(a,tau,[lwork,overwrite_a])
    
    Wrapper for ``cungrq``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    tau : input rank-1 array('F') with bounds (k)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*m
    
    Returns
    -------
    q : rank-2 array('F') with bounds (m,n) and a storage
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def cunmqr(side, trans, a, tau, c, lwork, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    cq,work,info = cunmqr(side,trans,a,tau,c,lwork,[overwrite_c])
    
    Wrapper for ``cunmqr``.
    
    Parameters
    ----------
    side : input string(len=1)
    trans : input string(len=1)
    a : input rank-2 array('F') with bounds (lda,k)
    tau : input rank-1 array('F') with bounds (k)
    c : input rank-2 array('F') with bounds (ldc,n)
    lwork : input int
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    cq : rank-2 array('F') with bounds (ldc,n) and c storage
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dgbsv(kl, ku, ab, b, overwrite_ab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lub,piv,x,info = dgbsv(kl,ku,ab,b,[overwrite_ab,overwrite_b])
    
    Wrapper for ``dgbsv``.
    
    Parameters
    ----------
    kl : input int
    ku : input int
    ab : input rank-2 array('d') with bounds (2*kl+ku+1,n)
    b : input rank-2 array('d') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    lub : rank-2 array('d') with bounds (2*kl+ku+1,n) and ab storage
    piv : rank-1 array('i') with bounds (n)
    x : rank-2 array('d') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def dgbtrf(ab, kl, ku, m=None, n=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    lu,ipiv,info = dgbtrf(ab,kl,ku,[m,n,ldab,overwrite_ab])
    
    Wrapper for ``dgbtrf``.
    
    Parameters
    ----------
    ab : input rank-2 array('d') with bounds (ldab,*)
    kl : input int
    ku : input int
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(ab,1)
    n : input int, optional
        Default: shape(ab,1)
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    
    Returns
    -------
    lu : rank-2 array('d') with bounds (ldab,*) and ab storage
    ipiv : rank-1 array('i') with bounds (MIN(m,n))
    info : int
    """
    pass

def dgbtrs(ab, kl, ku, b, ipiv, trans=None, n=None, ldab=None, ldb=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = dgbtrs(ab,kl,ku,b,ipiv,[trans,n,ldab,ldb,overwrite_b])
    
    Wrapper for ``dgbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('d') with bounds (ldab,*)
    kl : input int
    ku : input int
    b : input rank-2 array('d') with bounds (ldb,*)
    ipiv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    n : input int, optional
        Default: shape(ab,1)
    ldab : input int, optional
        Default: shape(ab,0)
    ldb : input int, optional
        Default: shape(b,0)
    
    Returns
    -------
    x : rank-2 array('d') with bounds (ldb,*) and b storage
    info : int
    """
    pass

def dgebal(a, scale=None, permute=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ba,lo,hi,pivscale,info = dgebal(a,[scale,permute,overwrite_a])
    
    Wrapper for ``dgebal``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    scale : input int, optional
        Default: 0
    permute : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    ba : rank-2 array('d') with bounds (m,n) and a storage
    lo : int
    hi : int
    pivscale : rank-1 array('d') with bounds (n)
    info : int
    """
    pass

def dgees(dselect, a, compute_v=None, sort_t=None, lwork=None, dselect_extra_args=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    t,sdim,wr,wi,vs,work,info = dgees(dselect,a,[compute_v,sort_t,lwork,dselect_extra_args,overwrite_a])
    
    Wrapper for ``dgees``.
    
    Parameters
    ----------
    dselect : call-back function
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    sort_t : input int, optional
        Default: 0
    dselect_extra_args : input tuple, optional
        Default: ()
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n
    
    Returns
    -------
    t : rank-2 array('d') with bounds (n,n) and a storage
    sdim : int
    wr : rank-1 array('d') with bounds (n)
    wi : rank-1 array('d') with bounds (n)
    vs : rank-2 array('d') with bounds (ldvs,n)
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def dselect(arg1,arg2): return dselect
      Required arguments:
        arg1 : input float
        arg2 : input float
      Return objects:
        dselect : int
    """
    pass

def dgeev(a, compute_vl=None, compute_vr=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    wr,wi,vl,vr,info = dgeev(a,[compute_vl,compute_vr,lwork,overwrite_a])
    
    Wrapper for ``dgeev``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 4*n
    
    Returns
    -------
    wr : rank-1 array('d') with bounds (n)
    wi : rank-1 array('d') with bounds (n)
    vl : rank-2 array('d') with bounds (ldvl,n)
    vr : rank-2 array('d') with bounds (ldvr,n)
    info : int
    """
    pass

def dgeev_lwork(n, compute_vl=None, compute_vr=None): # real signature unknown; restored from __doc__
    """
    work,info = dgeev_lwork(n,[compute_vl,compute_vr])
    
    Wrapper for ``dgeev_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgegv(*args, **kwds): # reliably restored by inspect
    """
    `dgegv` is deprecated!
    The `*gegv` family of routines has been deprecated in
    LAPACK 3.6.0 in favor of the `*ggev` family of routines.
    The corresponding wrappers will be removed from SciPy in
    a future release.
    
    alphar,alphai,beta,vl,vr,info = dgegv(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``dgegv``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 8*n
    
    Returns
    -------
    alphar : rank-1 array('d') with bounds (n)
    alphai : rank-1 array('d') with bounds (n)
    beta : rank-1 array('d') with bounds (n)
    vl : rank-2 array('d') with bounds (ldvl,n)
    vr : rank-2 array('d') with bounds (ldvr,n)
    info : int
    """
    pass

def dgehrd(a, lo=None, hi=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ht,tau,info = dgehrd(a,[lo,hi,lwork,overwrite_a])
    
    Wrapper for ``dgehrd``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(n,1)
    
    Returns
    -------
    ht : rank-2 array('d') with bounds (n,n) and a storage
    tau : rank-1 array('d') with bounds (n - 1)
    info : int
    """
    pass

def dgehrd_lwork(n, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    work,info = dgehrd_lwork(n,[lo,hi])
    
    Wrapper for ``dgehrd_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgelsd(a, b, lwork, size_iwork, cond=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,s,rank,info = dgelsd(a,b,lwork,size_iwork,[cond,overwrite_a,overwrite_b])
    
    Wrapper for ``dgelsd``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    b : input rank-2 array('d') with bounds (maxmn,nrhs)
    lwork : input int
    size_iwork : input int
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    cond : input float, optional
        Default: -1.0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (maxmn,nrhs) and b storage
    s : rank-1 array('d') with bounds (minmn)
    rank : int
    info : int
    """
    pass

def dgelsd_lwork(m, n, nrhs, cond=None, lwork=None): # real signature unknown; restored from __doc__
    """
    work,iwork,info = dgelsd_lwork(m,n,nrhs,[cond,lwork])
    
    Wrapper for ``dgelsd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : float
    iwork : int
    info : int
    """
    pass

def dgelss(a, b, cond=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    v,x,s,rank,work,info = dgelss(a,b,[cond,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``dgelss``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    b : input rank-2 array('d') with bounds (maxmn,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: 3*minmn+MAX(2*minmn,MAX(maxmn,nrhs))
    
    Returns
    -------
    v : rank-2 array('d') with bounds (m,n) and a storage
    x : rank-2 array('d') with bounds (maxmn,nrhs) and b storage
    s : rank-1 array('d') with bounds (minmn)
    rank : int
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dgelss_lwork(m, n, nrhs, cond=None, lwork=None): # real signature unknown; restored from __doc__
    """
    work,info = dgelss_lwork(m,n,nrhs,[cond,lwork])
    
    Wrapper for ``dgelss_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgelsy(a, b, jptv, cond, lwork, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    v,x,j,rank,info = dgelsy(a,b,jptv,cond,lwork,[overwrite_a,overwrite_b])
    
    Wrapper for ``dgelsy``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    b : input rank-2 array('d') with bounds (maxmn,nrhs)
    jptv : input rank-1 array('i') with bounds (n)
    cond : input float
    lwork : input int
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    v : rank-2 array('d') with bounds (m,n) and a storage
    x : rank-2 array('d') with bounds (maxmn,nrhs) and b storage
    j : rank-1 array('i') with bounds (n) and jptv storage
    rank : int
    info : int
    """
    pass

def dgelsy_lwork(m, n, nrhs, cond, lwork=None): # real signature unknown; restored from __doc__
    """
    work,info = dgelsy_lwork(m,n,nrhs,cond,[lwork])
    
    Wrapper for ``dgelsy_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    cond : input float
    
    Other Parameters
    ----------------
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgeqp3(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,jpvt,tau,work,info = dgeqp3(a,[lwork,overwrite_a])
    
    Wrapper for ``dgeqp3``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*(n+1)
    
    Returns
    -------
    qr : rank-2 array('d') with bounds (m,n) and a storage
    jpvt : rank-1 array('i') with bounds (n)
    tau : rank-1 array('d') with bounds (MIN(m,n))
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dgeqrf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,work,info = dgeqrf(a,[lwork,overwrite_a])
    
    Wrapper for ``dgeqrf``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n
    
    Returns
    -------
    qr : rank-2 array('d') with bounds (m,n) and a storage
    tau : rank-1 array('d') with bounds (MIN(m,n))
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dgerqf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,work,info = dgerqf(a,[lwork,overwrite_a])
    
    Wrapper for ``dgerqf``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*m
    
    Returns
    -------
    qr : rank-2 array('d') with bounds (m,n) and a storage
    tau : rank-1 array('d') with bounds (MIN(m,n))
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dgesdd(a, compute_uv=None, full_matrices=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    u,s,vt,info = dgesdd(a,[compute_uv,full_matrices,lwork,overwrite_a])
    
    Wrapper for ``dgesdd``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    lwork : input int, optional
        Default: (compute_uv?4*minmn*minmn+MAX(m,n)+9*minmn:MAX(14*minmn+4,10*minmn+2+25*(25+8))+MAX(m,n))
    
    Returns
    -------
    u : rank-2 array('d') with bounds (u0,u1)
    s : rank-1 array('d') with bounds (minmn)
    vt : rank-2 array('d') with bounds (vt0,vt1)
    info : int
    """
    pass

def dgesdd_lwork(m, n, compute_uv=None, full_matrices=None): # real signature unknown; restored from __doc__
    """
    work,info = dgesdd_lwork(m,n,[compute_uv,full_matrices])
    
    Wrapper for ``dgesdd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgesv(a, b, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lu,piv,x,info = dgesv(a,b,[overwrite_a,overwrite_b])
    
    Wrapper for ``dgesv``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('d') with bounds (n,n) and a storage
    piv : rank-1 array('i') with bounds (n)
    x : rank-2 array('d') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def dgesvd(a, compute_uv=None, full_matrices=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    u,s,vt,info = dgesvd(a,[compute_uv,full_matrices,lwork,overwrite_a])
    
    Wrapper for ``dgesvd``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    lwork : input int, optional
        Default: MAX(1,MAX(3*minmn+MAX(m,n),5*minmn))
    
    Returns
    -------
    u : rank-2 array('d') with bounds (u0,u1)
    s : rank-1 array('d') with bounds (minmn)
    vt : rank-2 array('d') with bounds (vt0,vt1)
    info : int
    """
    pass

def dgesvd_lwork(m, n, compute_uv=None, full_matrices=None): # real signature unknown; restored from __doc__
    """
    work,info = dgesvd_lwork(m,n,[compute_uv,full_matrices])
    
    Wrapper for ``dgesvd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgetrf(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    lu,piv,info = dgetrf(a,[overwrite_a])
    
    Wrapper for ``dgetrf``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('d') with bounds (m,n) and a storage
    piv : rank-1 array('i') with bounds (MIN(m,n))
    info : int
    """
    pass

def dgetri(lu, piv, lwork=None, overwrite_lu=None): # real signature unknown; restored from __doc__
    """
    inv_a,info = dgetri(lu,piv,[lwork,overwrite_lu])
    
    Wrapper for ``dgetri``.
    
    Parameters
    ----------
    lu : input rank-2 array('d') with bounds (n,n)
    piv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_lu : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n
    
    Returns
    -------
    inv_a : rank-2 array('d') with bounds (n,n) and lu storage
    info : int
    """
    pass

def dgetri_lwork(n): # real signature unknown; restored from __doc__
    """
    work,info = dgetri_lwork(n)
    
    Wrapper for ``dgetri_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgetrs(lu, piv, b, trans=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = dgetrs(lu,piv,b,[trans,overwrite_b])
    
    Wrapper for ``dgetrs``.
    
    Parameters
    ----------
    lu : input rank-2 array('d') with bounds (n,n)
    piv : input rank-1 array('i') with bounds (n)
    b : input rank-2 array('d') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def dgges(dselect, a, b, jobvsl=None, jobvsr=None, sort_t=None, ldvsl=None, ldvsr=None, lwork=None, dselect_extra_args=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,b,sdim,alphar,alphai,beta,vsl,vsr,work,info = dgges(dselect,a,b,[jobvsl,jobvsr,sort_t,ldvsl,ldvsr,lwork,dselect_extra_args,overwrite_a,overwrite_b])
    
    Wrapper for ``dgges``.
    
    Parameters
    ----------
    dselect : call-back function
    a : input rank-2 array('d') with bounds (lda,*)
    b : input rank-2 array('d') with bounds (ldb,*)
    
    Other Parameters
    ----------------
    jobvsl : input int, optional
        Default: 1
    jobvsr : input int, optional
        Default: 1
    sort_t : input int, optional
        Default: 0
    dselect_extra_args : input tuple, optional
        Default: ()
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    ldvsl : input int, optional
        Default: ((jobvsl==1)?n:1)
    ldvsr : input int, optional
        Default: ((jobvsr==1)?n:1)
    lwork : input int, optional
        Default: 8*n+16
    
    Returns
    -------
    a : rank-2 array('d') with bounds (lda,*)
    b : rank-2 array('d') with bounds (ldb,*)
    sdim : int
    alphar : rank-1 array('d') with bounds (n)
    alphai : rank-1 array('d') with bounds (n)
    beta : rank-1 array('d') with bounds (n)
    vsl : rank-2 array('d') with bounds (ldvsl,n)
    vsr : rank-2 array('d') with bounds (ldvsr,n)
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def dselect(alphar,alphai,beta): return dselect
      Required arguments:
        alphar : input float
        alphai : input float
        beta : input float
      Return objects:
        dselect : int
    """
    pass

def dggev(a, b, compute_vl=None, compute_vr=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    alphar,alphai,beta,vl,vr,work,info = dggev(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``dggev``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 8*n
    
    Returns
    -------
    alphar : rank-1 array('d') with bounds (n)
    alphai : rank-1 array('d') with bounds (n)
    beta : rank-1 array('d') with bounds (n)
    vl : rank-2 array('d') with bounds (ldvl,n)
    vr : rank-2 array('d') with bounds (ldvr,n)
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dgtsv(dl, d, du, b, overwrite_dl=None, overwrite_d=None, overwrite_du=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    du2,d,du,x,info = dgtsv(dl,d,du,b,[overwrite_dl,overwrite_d,overwrite_du,overwrite_b])
    
    Wrapper for ``dgtsv``.
    
    Parameters
    ----------
    dl : input rank-1 array('d') with bounds (n - 1)
    d : input rank-1 array('d') with bounds (*)
    du : input rank-1 array('d') with bounds (n - 1)
    b : input rank-2 array('d') with bounds (*,*)
    
    Other Parameters
    ----------------
    overwrite_dl : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    overwrite_du : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    du2 : rank-1 array('d') with bounds (n - 1) and dl storage
    d : rank-1 array('d') with bounds (*)
    du : rank-1 array('d') with bounds (n - 1)
    x : rank-2 array('d') with bounds (*,*) and b storage
    info : int
    """
    pass

def dlamch(cmach): # real signature unknown; restored from __doc__
    """
    dlamch = dlamch(cmach)
    
    Wrapper for ``dlamch``.
    
    Parameters
    ----------
    cmach : input string(len=1)
    
    Returns
    -------
    dlamch : float
    """
    pass

def dlange(norm, a): # real signature unknown; restored from __doc__
    """
    n2 = dlange(norm,a)
    
    Wrapper for ``dlange``.
    
    Parameters
    ----------
    norm : input string(len=1)
    a : input rank-2 array('d') with bounds (m,n)
    
    Returns
    -------
    n2 : float
    """
    pass

def dlarf(v, tau, c, work, side=None, incv=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = dlarf(v,tau,c,work,[side,incv,overwrite_c])
    
    Wrapper for ``dlarf``.
    
    Parameters
    ----------
    v : input rank-1 array('d') with bounds (*)
    tau : input float
    c : input rank-2 array('d') with bounds (m,n)
    work : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    incv : input int, optional
        Default: 1
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (m,n)
    """
    pass

def dlarfg(n, alpha, x, incx=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    alpha,x,tau = dlarfg(n,alpha,x,[incx,overwrite_x])
    
    Wrapper for ``dlarfg``.
    
    Parameters
    ----------
    n : input int
    alpha : input float
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    alpha : float
    x : rank-1 array('d') with bounds (*)
    tau : float
    """
    pass

def dlartg(f, g): # real signature unknown; restored from __doc__
    """
    cs,sn,r = dlartg(f,g)
    
    Wrapper for ``dlartg``.
    
    Parameters
    ----------
    f : input float
    g : input float
    
    Returns
    -------
    cs : float
    sn : float
    r : float
    """
    pass

def dlasd4(i, d, z, rho=None): # real signature unknown; restored from __doc__
    """
    delta,sigma,work,info = dlasd4(i,d,z,[rho])
    
    Wrapper for ``dlasd4``.
    
    Parameters
    ----------
    i : input int
    d : input rank-1 array('d') with bounds (n)
    z : input rank-1 array('d') with bounds (n)
    
    Other Parameters
    ----------------
    rho : input float, optional
        Default: 1.0
    
    Returns
    -------
    delta : rank-1 array('d') with bounds (n)
    sigma : float
    work : rank-1 array('d') with bounds (n)
    info : int
    """
    pass

def dlaswp(a, piv, k1=None, k2=None, off=None, inc=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = dlaswp(a,piv,[k1,k2,off,inc,overwrite_a])
    
    Wrapper for ``dlaswp``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (nrows,n)
    piv : input rank-1 array('i') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    k1 : input int, optional
        Default: 0
    k2 : input int, optional
        Default: len(piv)-1
    off : input int, optional
        Default: 0
    inc : input int, optional
        Default: 1
    
    Returns
    -------
    a : rank-2 array('d') with bounds (nrows,n)
    """
    pass

def dlauum(c, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    a,info = dlauum(c,[lower,overwrite_c])
    
    Wrapper for ``dlauum``.
    
    Parameters
    ----------
    c : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('d') with bounds (n,n) and c storage
    info : int
    """
    pass

def dorghr(a, tau, lo=None, hi=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ht,info = dorghr(a,tau,[lo,hi,lwork,overwrite_a])
    
    Wrapper for ``dorghr``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    tau : input rank-1 array('d') with bounds (n - 1)
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: hi-lo
    
    Returns
    -------
    ht : rank-2 array('d') with bounds (n,n) and a storage
    info : int
    """
    pass

def dorghr_lwork(n, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    work,info = dorghr_lwork(n,[lo,hi])
    
    Wrapper for ``dorghr_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dorgqr(a, tau, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    q,work,info = dorgqr(a,tau,[lwork,overwrite_a])
    
    Wrapper for ``dorgqr``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    tau : input rank-1 array('d') with bounds (k)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n
    
    Returns
    -------
    q : rank-2 array('d') with bounds (m,n) and a storage
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dorgrq(a, tau, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    q,work,info = dorgrq(a,tau,[lwork,overwrite_a])
    
    Wrapper for ``dorgrq``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    tau : input rank-1 array('d') with bounds (k)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*m
    
    Returns
    -------
    q : rank-2 array('d') with bounds (m,n) and a storage
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dormqr(side, trans, a, tau, c, lwork, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    cq,work,info = dormqr(side,trans,a,tau,c,lwork,[overwrite_c])
    
    Wrapper for ``dormqr``.
    
    Parameters
    ----------
    side : input string(len=1)
    trans : input string(len=1)
    a : input rank-2 array('d') with bounds (lda,k)
    tau : input rank-1 array('d') with bounds (k)
    c : input rank-2 array('d') with bounds (ldc,n)
    lwork : input int
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    cq : rank-2 array('d') with bounds (ldc,n) and c storage
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dpbsv(ab, b, lower=None, ldab=None, overwrite_ab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    c,x,info = dpbsv(ab,b,[lower,ldab,overwrite_ab,overwrite_b])
    
    Wrapper for ``dpbsv``.
    
    Parameters
    ----------
    ab : input rank-2 array('d') with bounds (ldab,n)
    b : input rank-2 array('d') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (ldab,n) and ab storage
    x : rank-2 array('d') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def dpbtrf(ab, lower=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    c,info = dpbtrf(ab,[lower,ldab,overwrite_ab])
    
    Wrapper for ``dpbtrf``.
    
    Parameters
    ----------
    ab : input rank-2 array('d') with bounds (ldab,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    
    Returns
    -------
    c : rank-2 array('d') with bounds (ldab,n) and ab storage
    info : int
    """
    pass

def dpbtrs(ab, b, lower=None, ldab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = dpbtrs(ab,b,[lower,ldab,overwrite_b])
    
    Wrapper for ``dpbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('d') with bounds (ldab,n)
    b : input rank-2 array('d') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def dposv(a, b, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    c,x,info = dposv(a,b,[lower,overwrite_a,overwrite_b])
    
    Wrapper for ``dposv``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (n,n) and a storage
    x : rank-2 array('d') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def dpotrf(a, lower=None, clean=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,info = dpotrf(a,[lower,clean,overwrite_a])
    
    Wrapper for ``dpotrf``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    clean : input int, optional
        Default: 1
    
    Returns
    -------
    c : rank-2 array('d') with bounds (n,n) and a storage
    info : int
    """
    pass

def dpotri(c, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    inv_a,info = dpotri(c,[lower,overwrite_c])
    
    Wrapper for ``dpotri``.
    
    Parameters
    ----------
    c : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    inv_a : rank-2 array('d') with bounds (n,n) and c storage
    info : int
    """
    pass

def dpotrs(c, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = dpotrs(c,b,[lower,overwrite_b])
    
    Wrapper for ``dpotrs``.
    
    Parameters
    ----------
    c : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def dptsv(d, e, b, overwrite_d=None, overwrite_e=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    d,du,x,info = dptsv(d,e,b,[overwrite_d,overwrite_e,overwrite_b])
    
    Wrapper for ``dptsv``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (*)
    e : input rank-1 array('d') with bounds (n - 1)
    b : input rank-2 array('d') with bounds (*,*)
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    d : rank-1 array('d') with bounds (*)
    du : rank-1 array('d') with bounds (n - 1) and e storage
    x : rank-2 array('d') with bounds (*,*) and b storage
    info : int
    """
    pass

def dsbev(ab, compute_v=None, lower=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,info = dsbev(ab,[compute_v,lower,ldab,overwrite_ab])
    
    Wrapper for ``dsbev``.
    
    Parameters
    ----------
    ab : input rank-2 array('d') with bounds (ldab,*)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    z : rank-2 array('d') with bounds (ldz,ldz)
    info : int
    """
    pass

def dsbevd(ab, compute_v=None, lower=None, ldab=None, liwork=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,info = dsbevd(ab,[compute_v,lower,ldab,liwork,overwrite_ab])
    
    Wrapper for ``dsbevd``.
    
    Parameters
    ----------
    ab : input rank-2 array('d') with bounds (ldab,*)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    liwork : input int, optional
        Default: (compute_v?3+5*n:1)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    z : rank-2 array('d') with bounds (ldz,ldz)
    info : int
    """
    pass

def dsbevx(ab, vl, vu, il, iu, ldab=None, compute_v=None, range=None, lower=None, abstol=None, mmax=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,m,ifail,info = dsbevx(ab,vl,vu,il,iu,[ldab,compute_v,range,lower,abstol,mmax,overwrite_ab])
    
    Wrapper for ``dsbevx``.
    
    Parameters
    ----------
    ab : input rank-2 array('d') with bounds (ldab,*)
    vl : input float
    vu : input float
    il : input int
    iu : input int
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    ldab : input int, optional
        Default: shape(ab,0)
    compute_v : input int, optional
        Default: 1
    range : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    abstol : input float, optional
        Default: 0.0
    mmax : input int, optional
        Default: (compute_v?(range==2?(iu-il+1):n):1)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    z : rank-2 array('d') with bounds (ldz,mmax)
    m : int
    ifail : rank-1 array('i') with bounds ((compute_v?n:1))
    info : int
    """
    pass

def dsyev(a, compute_v=None, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,v,info = dsyev(a,[compute_v,lower,lwork,overwrite_a])
    
    Wrapper for ``dsyev``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n-1
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    v : rank-2 array('d') with bounds (n,n) and a storage
    info : int
    """
    pass

def dsyevd(a, compute_v=None, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,v,info = dsyevd(a,[compute_v,lower,lwork,overwrite_a])
    
    Wrapper for ``dsyevd``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: (compute_v?1+6*n+2*n*n:2*n+1)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    v : rank-2 array('d') with bounds (n,n) and a storage
    info : int
    """
    pass

def dsyevr(a, jobz=None, range=None, uplo=None, il=None, iu=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,z,info = dsyevr(a,[jobz,range,uplo,il,iu,lwork,overwrite_a])
    
    Wrapper for ``dsyevr``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    jobz : input string(len=1), optional
        Default: 'V'
    range : input string(len=1), optional
        Default: 'A'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    il : input int, optional
        Default: 1
    iu : input int, optional
        Default: n
    lwork : input int, optional
        Default: 26*n
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    z : rank-2 array('d') with bounds (n,m)
    info : int
    """
    pass

def dsygv(a, b, itype=None, jobz=None, uplo=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,w,info = dsygv(a,b,[itype,jobz,uplo,overwrite_a,overwrite_b])
    
    Wrapper for ``dsygv``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('d') with bounds (n,n)
    w : rank-1 array('d') with bounds (n)
    info : int
    """
    pass

def dsygvd(a, b, itype=None, jobz=None, uplo=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,w,info = dsygvd(a,b,[itype,jobz,uplo,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``dsygvd``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 1+6*n+2*n*n
    
    Returns
    -------
    a : rank-2 array('d') with bounds (n,n)
    w : rank-1 array('d') with bounds (n)
    info : int
    """
    pass

def dsygvx(a, b, iu, itype=None, jobz=None, uplo=None, il=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    w,z,ifail,info = dsygvx(a,b,iu,[itype,jobz,uplo,il,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``dsygvx``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,n)
    iu : input int
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    il : input int, optional
        Default: 1
    lwork : input int, optional
        Default: 8*n
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    z : rank-2 array('d') with bounds (n,m)
    ifail : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def dtgsen(select, a, b, q, z, lwork=None, liwork=None, overwrite_a=None, overwrite_b=None, overwrite_q=None, overwrite_z=None): # real signature unknown; restored from __doc__
    """
    a,b,alphar,alphai,beta,q,z,m,pl,pr,dif,work,iwork,info = dtgsen(select,a,b,q,z,[lwork,liwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])
    
    Wrapper for ``dtgsen``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    a : input rank-2 array('d') with bounds (lda,*)
    b : input rank-2 array('d') with bounds (ldb,*)
    q : input rank-2 array('d') with bounds (ldq,*)
    z : input rank-2 array('d') with bounds (ldz,*)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    overwrite_z : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(4*n+16,2*m*(n-m))
    liwork : input int, optional
        Default: n+6
    
    Returns
    -------
    a : rank-2 array('d') with bounds (lda,*)
    b : rank-2 array('d') with bounds (ldb,*)
    alphar : rank-1 array('d') with bounds (n)
    alphai : rank-1 array('d') with bounds (n)
    beta : rank-1 array('d') with bounds (n)
    q : rank-2 array('d') with bounds (ldq,*)
    z : rank-2 array('d') with bounds (ldz,*)
    m : int
    pl : float
    pr : float
    dif : rank-1 array('d') with bounds (2)
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    iwork : rank-1 array('i') with bounds (MAX(1,liwork))
    info : int
    """
    pass

def dtrsyl(a, b, c, trana=None, tranb=None, isgn=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    x,scale,info = dtrsyl(a,b,c,[trana,tranb,isgn,overwrite_c])
    
    Wrapper for ``dtrsyl``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,m)
    b : input rank-2 array('d') with bounds (n,n)
    c : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    trana : input string(len=1), optional
        Default: 'N'
    tranb : input string(len=1), optional
        Default: 'N'
    isgn : input int, optional
        Default: 1
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (m,n) and c storage
    scale : float
    info : int
    """
    pass

def dtrtri(c, lower=None, unitdiag=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    inv_c,info = dtrtri(c,[lower,unitdiag,overwrite_c])
    
    Wrapper for ``dtrtri``.
    
    Parameters
    ----------
    c : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    
    Returns
    -------
    inv_c : rank-2 array('d') with bounds (n,n) and c storage
    info : int
    """
    pass

def dtrtrs(a, b, lower=None, trans=None, unitdiag=None, lda=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = dtrtrs(a,b,[lower,trans,unitdiag,lda,overwrite_b])
    
    Wrapper for ``dtrtrs``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (lda,n)
    b : input rank-2 array('d') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    lda : input int, optional
        Default: shape(a,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def ilaver(): # real signature unknown; restored from __doc__
    """
    major,minor,patch = ilaver()
    
    Wrapper for ``ilaver``.
    
    Returns
    -------
    major : int
    minor : int
    patch : int
    """
    pass

def sgbsv(kl, ku, ab, b, overwrite_ab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lub,piv,x,info = sgbsv(kl,ku,ab,b,[overwrite_ab,overwrite_b])
    
    Wrapper for ``sgbsv``.
    
    Parameters
    ----------
    kl : input int
    ku : input int
    ab : input rank-2 array('f') with bounds (2*kl+ku+1,n)
    b : input rank-2 array('f') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    lub : rank-2 array('f') with bounds (2*kl+ku+1,n) and ab storage
    piv : rank-1 array('i') with bounds (n)
    x : rank-2 array('f') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def sgbtrf(ab, kl, ku, m=None, n=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    lu,ipiv,info = sgbtrf(ab,kl,ku,[m,n,ldab,overwrite_ab])
    
    Wrapper for ``sgbtrf``.
    
    Parameters
    ----------
    ab : input rank-2 array('f') with bounds (ldab,*)
    kl : input int
    ku : input int
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(ab,1)
    n : input int, optional
        Default: shape(ab,1)
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    
    Returns
    -------
    lu : rank-2 array('f') with bounds (ldab,*) and ab storage
    ipiv : rank-1 array('i') with bounds (MIN(m,n))
    info : int
    """
    pass

def sgbtrs(ab, kl, ku, b, ipiv, trans=None, n=None, ldab=None, ldb=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = sgbtrs(ab,kl,ku,b,ipiv,[trans,n,ldab,ldb,overwrite_b])
    
    Wrapper for ``sgbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('f') with bounds (ldab,*)
    kl : input int
    ku : input int
    b : input rank-2 array('f') with bounds (ldb,*)
    ipiv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    n : input int, optional
        Default: shape(ab,1)
    ldab : input int, optional
        Default: shape(ab,0)
    ldb : input int, optional
        Default: shape(b,0)
    
    Returns
    -------
    x : rank-2 array('f') with bounds (ldb,*) and b storage
    info : int
    """
    pass

def sgebal(a, scale=None, permute=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ba,lo,hi,pivscale,info = sgebal(a,[scale,permute,overwrite_a])
    
    Wrapper for ``sgebal``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    scale : input int, optional
        Default: 0
    permute : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    ba : rank-2 array('f') with bounds (m,n) and a storage
    lo : int
    hi : int
    pivscale : rank-1 array('f') with bounds (n)
    info : int
    """
    pass

def sgees(sselect, a, compute_v=None, sort_t=None, lwork=None, sselect_extra_args=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    t,sdim,wr,wi,vs,work,info = sgees(sselect,a,[compute_v,sort_t,lwork,sselect_extra_args,overwrite_a])
    
    Wrapper for ``sgees``.
    
    Parameters
    ----------
    sselect : call-back function
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    sort_t : input int, optional
        Default: 0
    sselect_extra_args : input tuple, optional
        Default: ()
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n
    
    Returns
    -------
    t : rank-2 array('f') with bounds (n,n) and a storage
    sdim : int
    wr : rank-1 array('f') with bounds (n)
    wi : rank-1 array('f') with bounds (n)
    vs : rank-2 array('f') with bounds (ldvs,n)
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def sselect(arg1,arg2): return sselect
      Required arguments:
        arg1 : input float
        arg2 : input float
      Return objects:
        sselect : int
    """
    pass

def sgeev(a, compute_vl=None, compute_vr=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    wr,wi,vl,vr,info = sgeev(a,[compute_vl,compute_vr,lwork,overwrite_a])
    
    Wrapper for ``sgeev``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 4*n
    
    Returns
    -------
    wr : rank-1 array('f') with bounds (n)
    wi : rank-1 array('f') with bounds (n)
    vl : rank-2 array('f') with bounds (ldvl,n)
    vr : rank-2 array('f') with bounds (ldvr,n)
    info : int
    """
    pass

def sgeev_lwork(n, compute_vl=None, compute_vr=None): # real signature unknown; restored from __doc__
    """
    work,info = sgeev_lwork(n,[compute_vl,compute_vr])
    
    Wrapper for ``sgeev_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgegv(*args, **kwds): # reliably restored by inspect
    """
    `sgegv` is deprecated!
    The `*gegv` family of routines has been deprecated in
    LAPACK 3.6.0 in favor of the `*ggev` family of routines.
    The corresponding wrappers will be removed from SciPy in
    a future release.
    
    alphar,alphai,beta,vl,vr,info = sgegv(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``sgegv``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 8*n
    
    Returns
    -------
    alphar : rank-1 array('f') with bounds (n)
    alphai : rank-1 array('f') with bounds (n)
    beta : rank-1 array('f') with bounds (n)
    vl : rank-2 array('f') with bounds (ldvl,n)
    vr : rank-2 array('f') with bounds (ldvr,n)
    info : int
    """
    pass

def sgehrd(a, lo=None, hi=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ht,tau,info = sgehrd(a,[lo,hi,lwork,overwrite_a])
    
    Wrapper for ``sgehrd``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(n,1)
    
    Returns
    -------
    ht : rank-2 array('f') with bounds (n,n) and a storage
    tau : rank-1 array('f') with bounds (n - 1)
    info : int
    """
    pass

def sgehrd_lwork(n, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    work,info = sgehrd_lwork(n,[lo,hi])
    
    Wrapper for ``sgehrd_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgelsd(a, b, lwork, size_iwork, cond=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,s,rank,info = sgelsd(a,b,lwork,size_iwork,[cond,overwrite_a,overwrite_b])
    
    Wrapper for ``sgelsd``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    b : input rank-2 array('f') with bounds (maxmn,nrhs)
    lwork : input int
    size_iwork : input int
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    cond : input float, optional
        Default: -1.0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (maxmn,nrhs) and b storage
    s : rank-1 array('f') with bounds (minmn)
    rank : int
    info : int
    """
    pass

def sgelsd_lwork(m, n, nrhs, cond=None, lwork=None): # real signature unknown; restored from __doc__
    """
    work,iwork,info = sgelsd_lwork(m,n,nrhs,[cond,lwork])
    
    Wrapper for ``sgelsd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : float
    iwork : int
    info : int
    """
    pass

def sgelss(a, b, cond=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    v,x,s,rank,work,info = sgelss(a,b,[cond,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``sgelss``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    b : input rank-2 array('f') with bounds (maxmn,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: 3*minmn+MAX(2*minmn,MAX(maxmn,nrhs))
    
    Returns
    -------
    v : rank-2 array('f') with bounds (m,n) and a storage
    x : rank-2 array('f') with bounds (maxmn,nrhs) and b storage
    s : rank-1 array('f') with bounds (minmn)
    rank : int
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def sgelss_lwork(m, n, nrhs, cond=None, lwork=None): # real signature unknown; restored from __doc__
    """
    work,info = sgelss_lwork(m,n,nrhs,[cond,lwork])
    
    Wrapper for ``sgelss_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgelsy(a, b, jptv, cond, lwork, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    v,x,j,rank,info = sgelsy(a,b,jptv,cond,lwork,[overwrite_a,overwrite_b])
    
    Wrapper for ``sgelsy``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    b : input rank-2 array('f') with bounds (maxmn,nrhs)
    jptv : input rank-1 array('i') with bounds (n)
    cond : input float
    lwork : input int
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    v : rank-2 array('f') with bounds (m,n) and a storage
    x : rank-2 array('f') with bounds (maxmn,nrhs) and b storage
    j : rank-1 array('i') with bounds (n) and jptv storage
    rank : int
    info : int
    """
    pass

def sgelsy_lwork(m, n, nrhs, cond, lwork=None): # real signature unknown; restored from __doc__
    """
    work,info = sgelsy_lwork(m,n,nrhs,cond,[lwork])
    
    Wrapper for ``sgelsy_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    cond : input float
    
    Other Parameters
    ----------------
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgeqp3(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,jpvt,tau,work,info = sgeqp3(a,[lwork,overwrite_a])
    
    Wrapper for ``sgeqp3``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*(n+1)
    
    Returns
    -------
    qr : rank-2 array('f') with bounds (m,n) and a storage
    jpvt : rank-1 array('i') with bounds (n)
    tau : rank-1 array('f') with bounds (MIN(m,n))
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def sgeqrf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,work,info = sgeqrf(a,[lwork,overwrite_a])
    
    Wrapper for ``sgeqrf``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n
    
    Returns
    -------
    qr : rank-2 array('f') with bounds (m,n) and a storage
    tau : rank-1 array('f') with bounds (MIN(m,n))
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def sgerqf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,work,info = sgerqf(a,[lwork,overwrite_a])
    
    Wrapper for ``sgerqf``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*m
    
    Returns
    -------
    qr : rank-2 array('f') with bounds (m,n) and a storage
    tau : rank-1 array('f') with bounds (MIN(m,n))
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def sgesdd(a, compute_uv=None, full_matrices=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    u,s,vt,info = sgesdd(a,[compute_uv,full_matrices,lwork,overwrite_a])
    
    Wrapper for ``sgesdd``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    lwork : input int, optional
        Default: (compute_uv?4*minmn*minmn+MAX(m,n)+9*minmn:MAX(14*minmn+4,10*minmn+2+25*(25+8))+MAX(m,n))
    
    Returns
    -------
    u : rank-2 array('f') with bounds (u0,u1)
    s : rank-1 array('f') with bounds (minmn)
    vt : rank-2 array('f') with bounds (vt0,vt1)
    info : int
    """
    pass

def sgesdd_lwork(m, n, compute_uv=None, full_matrices=None): # real signature unknown; restored from __doc__
    """
    work,info = sgesdd_lwork(m,n,[compute_uv,full_matrices])
    
    Wrapper for ``sgesdd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgesv(a, b, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lu,piv,x,info = sgesv(a,b,[overwrite_a,overwrite_b])
    
    Wrapper for ``sgesv``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('f') with bounds (n,n) and a storage
    piv : rank-1 array('i') with bounds (n)
    x : rank-2 array('f') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def sgesvd(a, compute_uv=None, full_matrices=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    u,s,vt,info = sgesvd(a,[compute_uv,full_matrices,lwork,overwrite_a])
    
    Wrapper for ``sgesvd``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    lwork : input int, optional
        Default: MAX(1,MAX(3*minmn+MAX(m,n),5*minmn))
    
    Returns
    -------
    u : rank-2 array('f') with bounds (u0,u1)
    s : rank-1 array('f') with bounds (minmn)
    vt : rank-2 array('f') with bounds (vt0,vt1)
    info : int
    """
    pass

def sgesvd_lwork(m, n, compute_uv=None, full_matrices=None): # real signature unknown; restored from __doc__
    """
    work,info = sgesvd_lwork(m,n,[compute_uv,full_matrices])
    
    Wrapper for ``sgesvd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgetrf(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    lu,piv,info = sgetrf(a,[overwrite_a])
    
    Wrapper for ``sgetrf``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('f') with bounds (m,n) and a storage
    piv : rank-1 array('i') with bounds (MIN(m,n))
    info : int
    """
    pass

def sgetri(lu, piv, lwork=None, overwrite_lu=None): # real signature unknown; restored from __doc__
    """
    inv_a,info = sgetri(lu,piv,[lwork,overwrite_lu])
    
    Wrapper for ``sgetri``.
    
    Parameters
    ----------
    lu : input rank-2 array('f') with bounds (n,n)
    piv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_lu : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n
    
    Returns
    -------
    inv_a : rank-2 array('f') with bounds (n,n) and lu storage
    info : int
    """
    pass

def sgetri_lwork(n): # real signature unknown; restored from __doc__
    """
    work,info = sgetri_lwork(n)
    
    Wrapper for ``sgetri_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgetrs(lu, piv, b, trans=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = sgetrs(lu,piv,b,[trans,overwrite_b])
    
    Wrapper for ``sgetrs``.
    
    Parameters
    ----------
    lu : input rank-2 array('f') with bounds (n,n)
    piv : input rank-1 array('i') with bounds (n)
    b : input rank-2 array('f') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def sgges(sselect, a, b, jobvsl=None, jobvsr=None, sort_t=None, ldvsl=None, ldvsr=None, lwork=None, sselect_extra_args=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,b,sdim,alphar,alphai,beta,vsl,vsr,work,info = sgges(sselect,a,b,[jobvsl,jobvsr,sort_t,ldvsl,ldvsr,lwork,sselect_extra_args,overwrite_a,overwrite_b])
    
    Wrapper for ``sgges``.
    
    Parameters
    ----------
    sselect : call-back function
    a : input rank-2 array('f') with bounds (lda,*)
    b : input rank-2 array('f') with bounds (ldb,*)
    
    Other Parameters
    ----------------
    jobvsl : input int, optional
        Default: 1
    jobvsr : input int, optional
        Default: 1
    sort_t : input int, optional
        Default: 0
    sselect_extra_args : input tuple, optional
        Default: ()
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    ldvsl : input int, optional
        Default: ((jobvsl==1)?n:1)
    ldvsr : input int, optional
        Default: ((jobvsr==1)?n:1)
    lwork : input int, optional
        Default: 8*n+16
    
    Returns
    -------
    a : rank-2 array('f') with bounds (lda,*)
    b : rank-2 array('f') with bounds (ldb,*)
    sdim : int
    alphar : rank-1 array('f') with bounds (n)
    alphai : rank-1 array('f') with bounds (n)
    beta : rank-1 array('f') with bounds (n)
    vsl : rank-2 array('f') with bounds (ldvsl,n)
    vsr : rank-2 array('f') with bounds (ldvsr,n)
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def sselect(alphar,alphai,beta): return sselect
      Required arguments:
        alphar : input float
        alphai : input float
        beta : input float
      Return objects:
        sselect : int
    """
    pass

def sggev(a, b, compute_vl=None, compute_vr=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    alphar,alphai,beta,vl,vr,work,info = sggev(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``sggev``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 8*n
    
    Returns
    -------
    alphar : rank-1 array('f') with bounds (n)
    alphai : rank-1 array('f') with bounds (n)
    beta : rank-1 array('f') with bounds (n)
    vl : rank-2 array('f') with bounds (ldvl,n)
    vr : rank-2 array('f') with bounds (ldvr,n)
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def sgtsv(dl, d, du, b, overwrite_dl=None, overwrite_d=None, overwrite_du=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    du2,d,du,x,info = sgtsv(dl,d,du,b,[overwrite_dl,overwrite_d,overwrite_du,overwrite_b])
    
    Wrapper for ``sgtsv``.
    
    Parameters
    ----------
    dl : input rank-1 array('f') with bounds (n - 1)
    d : input rank-1 array('f') with bounds (*)
    du : input rank-1 array('f') with bounds (n - 1)
    b : input rank-2 array('f') with bounds (*,*)
    
    Other Parameters
    ----------------
    overwrite_dl : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    overwrite_du : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    du2 : rank-1 array('f') with bounds (n - 1) and dl storage
    d : rank-1 array('f') with bounds (*)
    du : rank-1 array('f') with bounds (n - 1)
    x : rank-2 array('f') with bounds (*,*) and b storage
    info : int
    """
    pass

def slamch(cmach): # real signature unknown; restored from __doc__
    """
    slamch = slamch(cmach)
    
    Wrapper for ``slamch``.
    
    Parameters
    ----------
    cmach : input string(len=1)
    
    Returns
    -------
    slamch : float
    """
    pass

def slange(norm, a): # real signature unknown; restored from __doc__
    """
    n2 = slange(norm,a)
    
    Wrapper for ``slange``.
    
    Parameters
    ----------
    norm : input string(len=1)
    a : input rank-2 array('f') with bounds (m,n)
    
    Returns
    -------
    n2 : float
    """
    pass

def slarf(v, tau, c, work, side=None, incv=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = slarf(v,tau,c,work,[side,incv,overwrite_c])
    
    Wrapper for ``slarf``.
    
    Parameters
    ----------
    v : input rank-1 array('f') with bounds (*)
    tau : input float
    c : input rank-2 array('f') with bounds (m,n)
    work : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    incv : input int, optional
        Default: 1
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (m,n)
    """
    pass

def slarfg(n, alpha, x, incx=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    alpha,x,tau = slarfg(n,alpha,x,[incx,overwrite_x])
    
    Wrapper for ``slarfg``.
    
    Parameters
    ----------
    n : input int
    alpha : input float
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    alpha : float
    x : rank-1 array('f') with bounds (*)
    tau : float
    """
    pass

def slartg(f, g): # real signature unknown; restored from __doc__
    """
    cs,sn,r = slartg(f,g)
    
    Wrapper for ``slartg``.
    
    Parameters
    ----------
    f : input float
    g : input float
    
    Returns
    -------
    cs : float
    sn : float
    r : float
    """
    pass

def slasd4(i, d, z, rho=None): # real signature unknown; restored from __doc__
    """
    delta,sigma,work,info = slasd4(i,d,z,[rho])
    
    Wrapper for ``slasd4``.
    
    Parameters
    ----------
    i : input int
    d : input rank-1 array('f') with bounds (n)
    z : input rank-1 array('f') with bounds (n)
    
    Other Parameters
    ----------------
    rho : input float, optional
        Default: 1.0
    
    Returns
    -------
    delta : rank-1 array('f') with bounds (n)
    sigma : float
    work : rank-1 array('f') with bounds (n)
    info : int
    """
    pass

def slaswp(a, piv, k1=None, k2=None, off=None, inc=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = slaswp(a,piv,[k1,k2,off,inc,overwrite_a])
    
    Wrapper for ``slaswp``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (nrows,n)
    piv : input rank-1 array('i') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    k1 : input int, optional
        Default: 0
    k2 : input int, optional
        Default: len(piv)-1
    off : input int, optional
        Default: 0
    inc : input int, optional
        Default: 1
    
    Returns
    -------
    a : rank-2 array('f') with bounds (nrows,n)
    """
    pass

def slauum(c, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    a,info = slauum(c,[lower,overwrite_c])
    
    Wrapper for ``slauum``.
    
    Parameters
    ----------
    c : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('f') with bounds (n,n) and c storage
    info : int
    """
    pass

def sorghr(a, tau, lo=None, hi=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ht,info = sorghr(a,tau,[lo,hi,lwork,overwrite_a])
    
    Wrapper for ``sorghr``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    tau : input rank-1 array('f') with bounds (n - 1)
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: hi-lo
    
    Returns
    -------
    ht : rank-2 array('f') with bounds (n,n) and a storage
    info : int
    """
    pass

def sorghr_lwork(n, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    work,info = sorghr_lwork(n,[lo,hi])
    
    Wrapper for ``sorghr_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sorgqr(a, tau, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    q,work,info = sorgqr(a,tau,[lwork,overwrite_a])
    
    Wrapper for ``sorgqr``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    tau : input rank-1 array('f') with bounds (k)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n
    
    Returns
    -------
    q : rank-2 array('f') with bounds (m,n) and a storage
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def sorgrq(a, tau, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    q,work,info = sorgrq(a,tau,[lwork,overwrite_a])
    
    Wrapper for ``sorgrq``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    tau : input rank-1 array('f') with bounds (k)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*m
    
    Returns
    -------
    q : rank-2 array('f') with bounds (m,n) and a storage
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def sormqr(side, trans, a, tau, c, lwork, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    cq,work,info = sormqr(side,trans,a,tau,c,lwork,[overwrite_c])
    
    Wrapper for ``sormqr``.
    
    Parameters
    ----------
    side : input string(len=1)
    trans : input string(len=1)
    a : input rank-2 array('f') with bounds (lda,k)
    tau : input rank-1 array('f') with bounds (k)
    c : input rank-2 array('f') with bounds (ldc,n)
    lwork : input int
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    cq : rank-2 array('f') with bounds (ldc,n) and c storage
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def spbsv(ab, b, lower=None, ldab=None, overwrite_ab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    c,x,info = spbsv(ab,b,[lower,ldab,overwrite_ab,overwrite_b])
    
    Wrapper for ``spbsv``.
    
    Parameters
    ----------
    ab : input rank-2 array('f') with bounds (ldab,n)
    b : input rank-2 array('f') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (ldab,n) and ab storage
    x : rank-2 array('f') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def spbtrf(ab, lower=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    c,info = spbtrf(ab,[lower,ldab,overwrite_ab])
    
    Wrapper for ``spbtrf``.
    
    Parameters
    ----------
    ab : input rank-2 array('f') with bounds (ldab,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    
    Returns
    -------
    c : rank-2 array('f') with bounds (ldab,n) and ab storage
    info : int
    """
    pass

def spbtrs(ab, b, lower=None, ldab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = spbtrs(ab,b,[lower,ldab,overwrite_b])
    
    Wrapper for ``spbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('f') with bounds (ldab,n)
    b : input rank-2 array('f') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def sposv(a, b, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    c,x,info = sposv(a,b,[lower,overwrite_a,overwrite_b])
    
    Wrapper for ``sposv``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (n,n) and a storage
    x : rank-2 array('f') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def spotrf(a, lower=None, clean=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,info = spotrf(a,[lower,clean,overwrite_a])
    
    Wrapper for ``spotrf``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    clean : input int, optional
        Default: 1
    
    Returns
    -------
    c : rank-2 array('f') with bounds (n,n) and a storage
    info : int
    """
    pass

def spotri(c, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    inv_a,info = spotri(c,[lower,overwrite_c])
    
    Wrapper for ``spotri``.
    
    Parameters
    ----------
    c : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    inv_a : rank-2 array('f') with bounds (n,n) and c storage
    info : int
    """
    pass

def spotrs(c, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = spotrs(c,b,[lower,overwrite_b])
    
    Wrapper for ``spotrs``.
    
    Parameters
    ----------
    c : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def sptsv(d, e, b, overwrite_d=None, overwrite_e=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    d,du,x,info = sptsv(d,e,b,[overwrite_d,overwrite_e,overwrite_b])
    
    Wrapper for ``sptsv``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (*)
    e : input rank-1 array('f') with bounds (n - 1)
    b : input rank-2 array('f') with bounds (*,*)
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    d : rank-1 array('f') with bounds (*)
    du : rank-1 array('f') with bounds (n - 1) and e storage
    x : rank-2 array('f') with bounds (*,*) and b storage
    info : int
    """
    pass

def ssbev(ab, compute_v=None, lower=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,info = ssbev(ab,[compute_v,lower,ldab,overwrite_ab])
    
    Wrapper for ``ssbev``.
    
    Parameters
    ----------
    ab : input rank-2 array('f') with bounds (ldab,*)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    z : rank-2 array('f') with bounds (ldz,ldz)
    info : int
    """
    pass

def ssbevd(ab, compute_v=None, lower=None, ldab=None, liwork=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,info = ssbevd(ab,[compute_v,lower,ldab,liwork,overwrite_ab])
    
    Wrapper for ``ssbevd``.
    
    Parameters
    ----------
    ab : input rank-2 array('f') with bounds (ldab,*)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    liwork : input int, optional
        Default: (compute_v?3+5*n:1)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    z : rank-2 array('f') with bounds (ldz,ldz)
    info : int
    """
    pass

def ssbevx(ab, vl, vu, il, iu, ldab=None, compute_v=None, range=None, lower=None, abstol=None, mmax=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,m,ifail,info = ssbevx(ab,vl,vu,il,iu,[ldab,compute_v,range,lower,abstol,mmax,overwrite_ab])
    
    Wrapper for ``ssbevx``.
    
    Parameters
    ----------
    ab : input rank-2 array('f') with bounds (ldab,*)
    vl : input float
    vu : input float
    il : input int
    iu : input int
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    ldab : input int, optional
        Default: shape(ab,0)
    compute_v : input int, optional
        Default: 1
    range : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    abstol : input float, optional
        Default: 0.0
    mmax : input int, optional
        Default: (compute_v?(range==2?(iu-il+1):n):1)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    z : rank-2 array('f') with bounds (ldz,mmax)
    m : int
    ifail : rank-1 array('i') with bounds ((compute_v?n:1))
    info : int
    """
    pass

def ssyev(a, compute_v=None, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,v,info = ssyev(a,[compute_v,lower,lwork,overwrite_a])
    
    Wrapper for ``ssyev``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n-1
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    v : rank-2 array('f') with bounds (n,n) and a storage
    info : int
    """
    pass

def ssyevd(a, compute_v=None, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,v,info = ssyevd(a,[compute_v,lower,lwork,overwrite_a])
    
    Wrapper for ``ssyevd``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: (compute_v?1+6*n+2*n*n:2*n+1)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    v : rank-2 array('f') with bounds (n,n) and a storage
    info : int
    """
    pass

def ssyevr(a, jobz=None, range=None, uplo=None, il=None, iu=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,z,info = ssyevr(a,[jobz,range,uplo,il,iu,lwork,overwrite_a])
    
    Wrapper for ``ssyevr``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    jobz : input string(len=1), optional
        Default: 'V'
    range : input string(len=1), optional
        Default: 'A'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    il : input int, optional
        Default: 1
    iu : input int, optional
        Default: n
    lwork : input int, optional
        Default: 26*n
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    z : rank-2 array('f') with bounds (n,m)
    info : int
    """
    pass

def ssygv(a, b, itype=None, jobz=None, uplo=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,w,info = ssygv(a,b,[itype,jobz,uplo,overwrite_a,overwrite_b])
    
    Wrapper for ``ssygv``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('f') with bounds (n,n)
    w : rank-1 array('f') with bounds (n)
    info : int
    """
    pass

def ssygvd(a, b, itype=None, jobz=None, uplo=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,w,info = ssygvd(a,b,[itype,jobz,uplo,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``ssygvd``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 1+6*n+2*n*n
    
    Returns
    -------
    a : rank-2 array('f') with bounds (n,n)
    w : rank-1 array('f') with bounds (n)
    info : int
    """
    pass

def ssygvx(a, b, iu, itype=None, jobz=None, uplo=None, il=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    w,z,ifail,info = ssygvx(a,b,iu,[itype,jobz,uplo,il,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``ssygvx``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,n)
    iu : input int
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    il : input int, optional
        Default: 1
    lwork : input int, optional
        Default: 8*n
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    z : rank-2 array('f') with bounds (n,m)
    ifail : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def stgsen(select, a, b, q, z, lwork=None, liwork=None, overwrite_a=None, overwrite_b=None, overwrite_q=None, overwrite_z=None): # real signature unknown; restored from __doc__
    """
    a,b,alphar,alphai,beta,q,z,m,pl,pr,dif,work,iwork,info = stgsen(select,a,b,q,z,[lwork,liwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])
    
    Wrapper for ``stgsen``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    a : input rank-2 array('f') with bounds (lda,*)
    b : input rank-2 array('f') with bounds (ldb,*)
    q : input rank-2 array('f') with bounds (ldq,*)
    z : input rank-2 array('f') with bounds (ldz,*)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    overwrite_z : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(4*n+16,2*m*(n-m))
    liwork : input int, optional
        Default: n+6
    
    Returns
    -------
    a : rank-2 array('f') with bounds (lda,*)
    b : rank-2 array('f') with bounds (ldb,*)
    alphar : rank-1 array('f') with bounds (n)
    alphai : rank-1 array('f') with bounds (n)
    beta : rank-1 array('f') with bounds (n)
    q : rank-2 array('f') with bounds (ldq,*)
    z : rank-2 array('f') with bounds (ldz,*)
    m : int
    pl : float
    pr : float
    dif : rank-1 array('f') with bounds (2)
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    iwork : rank-1 array('i') with bounds (MAX(1,liwork))
    info : int
    """
    pass

def strsyl(a, b, c, trana=None, tranb=None, isgn=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    x,scale,info = strsyl(a,b,c,[trana,tranb,isgn,overwrite_c])
    
    Wrapper for ``strsyl``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,m)
    b : input rank-2 array('f') with bounds (n,n)
    c : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    trana : input string(len=1), optional
        Default: 'N'
    tranb : input string(len=1), optional
        Default: 'N'
    isgn : input int, optional
        Default: 1
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (m,n) and c storage
    scale : float
    info : int
    """
    pass

def strtri(c, lower=None, unitdiag=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    inv_c,info = strtri(c,[lower,unitdiag,overwrite_c])
    
    Wrapper for ``strtri``.
    
    Parameters
    ----------
    c : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    
    Returns
    -------
    inv_c : rank-2 array('f') with bounds (n,n) and c storage
    info : int
    """
    pass

def strtrs(a, b, lower=None, trans=None, unitdiag=None, lda=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = strtrs(a,b,[lower,trans,unitdiag,lda,overwrite_b])
    
    Wrapper for ``strtrs``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (lda,n)
    b : input rank-2 array('f') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    lda : input int, optional
        Default: shape(a,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def zgbsv(kl, ku, ab, b, overwrite_ab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lub,piv,x,info = zgbsv(kl,ku,ab,b,[overwrite_ab,overwrite_b])
    
    Wrapper for ``zgbsv``.
    
    Parameters
    ----------
    kl : input int
    ku : input int
    ab : input rank-2 array('D') with bounds (2*kl+ku+1,n)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    lub : rank-2 array('D') with bounds (2*kl+ku+1,n) and ab storage
    piv : rank-1 array('i') with bounds (n)
    x : rank-2 array('D') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def zgbtrf(ab, kl, ku, m=None, n=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    lu,ipiv,info = zgbtrf(ab,kl,ku,[m,n,ldab,overwrite_ab])
    
    Wrapper for ``zgbtrf``.
    
    Parameters
    ----------
    ab : input rank-2 array('D') with bounds (ldab,*)
    kl : input int
    ku : input int
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(ab,1)
    n : input int, optional
        Default: shape(ab,1)
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    
    Returns
    -------
    lu : rank-2 array('D') with bounds (ldab,*) and ab storage
    ipiv : rank-1 array('i') with bounds (MIN(m,n))
    info : int
    """
    pass

def zgbtrs(ab, kl, ku, b, ipiv, trans=None, n=None, ldab=None, ldb=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = zgbtrs(ab,kl,ku,b,ipiv,[trans,n,ldab,ldb,overwrite_b])
    
    Wrapper for ``zgbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('D') with bounds (ldab,*)
    kl : input int
    ku : input int
    b : input rank-2 array('D') with bounds (ldb,*)
    ipiv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    n : input int, optional
        Default: shape(ab,1)
    ldab : input int, optional
        Default: shape(ab,0)
    ldb : input int, optional
        Default: shape(b,0)
    
    Returns
    -------
    x : rank-2 array('D') with bounds (ldb,*) and b storage
    info : int
    """
    pass

def zgebal(a, scale=None, permute=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ba,lo,hi,pivscale,info = zgebal(a,[scale,permute,overwrite_a])
    
    Wrapper for ``zgebal``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    scale : input int, optional
        Default: 0
    permute : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    ba : rank-2 array('D') with bounds (m,n) and a storage
    lo : int
    hi : int
    pivscale : rank-1 array('d') with bounds (n)
    info : int
    """
    pass

def zgees(zselect, a, compute_v=None, sort_t=None, lwork=None, zselect_extra_args=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    t,sdim,w,vs,work,info = zgees(zselect,a,[compute_v,sort_t,lwork,zselect_extra_args,overwrite_a])
    
    Wrapper for ``zgees``.
    
    Parameters
    ----------
    zselect : call-back function
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    sort_t : input int, optional
        Default: 0
    zselect_extra_args : input tuple, optional
        Default: ()
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n
    
    Returns
    -------
    t : rank-2 array('D') with bounds (n,n) and a storage
    sdim : int
    w : rank-1 array('D') with bounds (n)
    vs : rank-2 array('D') with bounds (ldvs,n)
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def zselect(arg): return zselect
      Required arguments:
        arg : input complex
      Return objects:
        zselect : int
    """
    pass

def zgeev(a, compute_vl=None, compute_vr=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,vl,vr,info = zgeev(a,[compute_vl,compute_vr,lwork,overwrite_a])
    
    Wrapper for ``zgeev``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 2*n
    
    Returns
    -------
    w : rank-1 array('D') with bounds (n)
    vl : rank-2 array('D') with bounds (ldvl,n)
    vr : rank-2 array('D') with bounds (ldvr,n)
    info : int
    """
    pass

def zgeev_lwork(n, compute_vl=None, compute_vr=None): # real signature unknown; restored from __doc__
    """
    work,info = zgeev_lwork(n,[compute_vl,compute_vr])
    
    Wrapper for ``zgeev_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgegv(*args, **kwds): # reliably restored by inspect
    """
    `zgegv` is deprecated!
    The `*gegv` family of routines has been deprecated in
    LAPACK 3.6.0 in favor of the `*ggev` family of routines.
    The corresponding wrappers will be removed from SciPy in
    a future release.
    
    alpha,beta,vl,vr,info = zgegv(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``zgegv``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 2*n
    
    Returns
    -------
    alpha : rank-1 array('D') with bounds (n)
    beta : rank-1 array('D') with bounds (n)
    vl : rank-2 array('D') with bounds (ldvl,n)
    vr : rank-2 array('D') with bounds (ldvr,n)
    info : int
    """
    pass

def zgehrd(a, lo=None, hi=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ht,tau,info = zgehrd(a,[lo,hi,lwork,overwrite_a])
    
    Wrapper for ``zgehrd``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(n,1)
    
    Returns
    -------
    ht : rank-2 array('D') with bounds (n,n) and a storage
    tau : rank-1 array('D') with bounds (n - 1)
    info : int
    """
    pass

def zgehrd_lwork(n, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    work,info = zgehrd_lwork(n,[lo,hi])
    
    Wrapper for ``zgehrd_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgelsd(a, b, lwork, size_rwork, size_iwork, cond=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,s,rank,info = zgelsd(a,b,lwork,size_rwork,size_iwork,[cond,overwrite_a,overwrite_b])
    
    Wrapper for ``zgelsd``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    b : input rank-2 array('D') with bounds (maxmn,nrhs)
    lwork : input int
    size_rwork : input int
    size_iwork : input int
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    cond : input float, optional
        Default: -1.0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (maxmn,nrhs) and b storage
    s : rank-1 array('d') with bounds (minmn)
    rank : int
    info : int
    """
    pass

def zgelsd_lwork(m, n, nrhs, cond=None, lwork=None): # real signature unknown; restored from __doc__
    """
    work,rwork,iwork,info = zgelsd_lwork(m,n,nrhs,[cond,lwork])
    
    Wrapper for ``zgelsd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : complex
    rwork : float
    iwork : int
    info : int
    """
    pass

def zgelss(a, b, cond=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    v,x,s,rank,work,info = zgelss(a,b,[cond,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``zgelss``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    b : input rank-2 array('D') with bounds (maxmn,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: 2*minmn+MAX(maxmn,nrhs)
    
    Returns
    -------
    v : rank-2 array('D') with bounds (m,n) and a storage
    x : rank-2 array('D') with bounds (maxmn,nrhs) and b storage
    s : rank-1 array('d') with bounds (minmn)
    rank : int
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def zgelss_lwork(m, n, nrhs, cond=None, lwork=None): # real signature unknown; restored from __doc__
    """
    work,info = zgelss_lwork(m,n,nrhs,[cond,lwork])
    
    Wrapper for ``zgelss_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgelsy(a, b, jptv, cond, lwork, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    v,x,j,rank,info = zgelsy(a,b,jptv,cond,lwork,[overwrite_a,overwrite_b])
    
    Wrapper for ``zgelsy``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    b : input rank-2 array('D') with bounds (maxmn,nrhs)
    jptv : input rank-1 array('i') with bounds (n)
    cond : input float
    lwork : input int
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    v : rank-2 array('D') with bounds (m,n) and a storage
    x : rank-2 array('D') with bounds (maxmn,nrhs) and b storage
    j : rank-1 array('i') with bounds (n) and jptv storage
    rank : int
    info : int
    """
    pass

def zgelsy_lwork(m, n, nrhs, cond, lwork=None): # real signature unknown; restored from __doc__
    """
    work,info = zgelsy_lwork(m,n,nrhs,cond,[lwork])
    
    Wrapper for ``zgelsy_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    cond : input float
    
    Other Parameters
    ----------------
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgeqp3(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,jpvt,tau,work,info = zgeqp3(a,[lwork,overwrite_a])
    
    Wrapper for ``zgeqp3``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*(n+1)
    
    Returns
    -------
    qr : rank-2 array('D') with bounds (m,n) and a storage
    jpvt : rank-1 array('i') with bounds (n)
    tau : rank-1 array('D') with bounds (MIN(m,n))
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def zgeqrf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,work,info = zgeqrf(a,[lwork,overwrite_a])
    
    Wrapper for ``zgeqrf``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n
    
    Returns
    -------
    qr : rank-2 array('D') with bounds (m,n) and a storage
    tau : rank-1 array('D') with bounds (MIN(m,n))
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def zgerqf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,work,info = zgerqf(a,[lwork,overwrite_a])
    
    Wrapper for ``zgerqf``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*m
    
    Returns
    -------
    qr : rank-2 array('D') with bounds (m,n) and a storage
    tau : rank-1 array('D') with bounds (MIN(m,n))
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def zgesdd(a, compute_uv=None, full_matrices=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    u,s,vt,info = zgesdd(a,[compute_uv,full_matrices,lwork,overwrite_a])
    
    Wrapper for ``zgesdd``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    lwork : input int, optional
        Default: (compute_uv?2*minmn*minmn+MAX(m,n)+2*minmn:2*minmn+MAX(m,n))
    
    Returns
    -------
    u : rank-2 array('D') with bounds (u0,u1)
    s : rank-1 array('d') with bounds (minmn)
    vt : rank-2 array('D') with bounds (vt0,vt1)
    info : int
    """
    pass

def zgesdd_lwork(m, n, compute_uv=None, full_matrices=None): # real signature unknown; restored from __doc__
    """
    work,info = zgesdd_lwork(m,n,[compute_uv,full_matrices])
    
    Wrapper for ``zgesdd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgesv(a, b, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lu,piv,x,info = zgesv(a,b,[overwrite_a,overwrite_b])
    
    Wrapper for ``zgesv``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('D') with bounds (n,n) and a storage
    piv : rank-1 array('i') with bounds (n)
    x : rank-2 array('D') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def zgesvd(a, compute_uv=None, full_matrices=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    u,s,vt,info = zgesvd(a,[compute_uv,full_matrices,lwork,overwrite_a])
    
    Wrapper for ``zgesvd``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    lwork : input int, optional
        Default: MAX(1,2*minmn+MAX(m,n))
    
    Returns
    -------
    u : rank-2 array('D') with bounds (u0,u1)
    s : rank-1 array('d') with bounds (minmn)
    vt : rank-2 array('D') with bounds (vt0,vt1)
    info : int
    """
    pass

def zgesvd_lwork(m, n, compute_uv=None, full_matrices=None): # real signature unknown; restored from __doc__
    """
    work,info = zgesvd_lwork(m,n,[compute_uv,full_matrices])
    
    Wrapper for ``zgesvd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgetrf(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    lu,piv,info = zgetrf(a,[overwrite_a])
    
    Wrapper for ``zgetrf``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('D') with bounds (m,n) and a storage
    piv : rank-1 array('i') with bounds (MIN(m,n))
    info : int
    """
    pass

def zgetri(lu, piv, lwork=None, overwrite_lu=None): # real signature unknown; restored from __doc__
    """
    inv_a,info = zgetri(lu,piv,[lwork,overwrite_lu])
    
    Wrapper for ``zgetri``.
    
    Parameters
    ----------
    lu : input rank-2 array('D') with bounds (n,n)
    piv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_lu : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n
    
    Returns
    -------
    inv_a : rank-2 array('D') with bounds (n,n) and lu storage
    info : int
    """
    pass

def zgetri_lwork(n): # real signature unknown; restored from __doc__
    """
    work,info = zgetri_lwork(n)
    
    Wrapper for ``zgetri_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgetrs(lu, piv, b, trans=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = zgetrs(lu,piv,b,[trans,overwrite_b])
    
    Wrapper for ``zgetrs``.
    
    Parameters
    ----------
    lu : input rank-2 array('D') with bounds (n,n)
    piv : input rank-1 array('i') with bounds (n)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def zgges(zselect, a, b, jobvsl=None, jobvsr=None, sort_t=None, ldvsl=None, ldvsr=None, lwork=None, zselect_extra_args=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,b,sdim,alpha,beta,vsl,vsr,work,info = zgges(zselect,a,b,[jobvsl,jobvsr,sort_t,ldvsl,ldvsr,lwork,zselect_extra_args,overwrite_a,overwrite_b])
    
    Wrapper for ``zgges``.
    
    Parameters
    ----------
    zselect : call-back function
    a : input rank-2 array('D') with bounds (lda,*)
    b : input rank-2 array('D') with bounds (ldb,*)
    
    Other Parameters
    ----------------
    jobvsl : input int, optional
        Default: 1
    jobvsr : input int, optional
        Default: 1
    sort_t : input int, optional
        Default: 0
    zselect_extra_args : input tuple, optional
        Default: ()
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    ldvsl : input int, optional
        Default: ((jobvsl==1)?n:1)
    ldvsr : input int, optional
        Default: ((jobvsr==1)?n:1)
    lwork : input int, optional
        Default: 2*n
    
    Returns
    -------
    a : rank-2 array('D') with bounds (lda,*)
    b : rank-2 array('D') with bounds (ldb,*)
    sdim : int
    alpha : rank-1 array('D') with bounds (n)
    beta : rank-1 array('D') with bounds (n)
    vsl : rank-2 array('D') with bounds (ldvsl,n)
    vsr : rank-2 array('D') with bounds (ldvsr,n)
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def zselect(alpha,beta): return zselect
      Required arguments:
        alpha : input complex
        beta : input complex
      Return objects:
        zselect : int
    """
    pass

def zggev(a, b, compute_vl=None, compute_vr=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    alpha,beta,vl,vr,work,info = zggev(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``zggev``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 2*n
    
    Returns
    -------
    alpha : rank-1 array('D') with bounds (n)
    beta : rank-1 array('D') with bounds (n)
    vl : rank-2 array('D') with bounds (ldvl,n)
    vr : rank-2 array('D') with bounds (ldvr,n)
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def zgtsv(dl, d, du, b, overwrite_dl=None, overwrite_d=None, overwrite_du=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    du2,d,du,x,info = zgtsv(dl,d,du,b,[overwrite_dl,overwrite_d,overwrite_du,overwrite_b])
    
    Wrapper for ``zgtsv``.
    
    Parameters
    ----------
    dl : input rank-1 array('D') with bounds (n - 1)
    d : input rank-1 array('D') with bounds (*)
    du : input rank-1 array('D') with bounds (n - 1)
    b : input rank-2 array('D') with bounds (*,*)
    
    Other Parameters
    ----------------
    overwrite_dl : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    overwrite_du : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    du2 : rank-1 array('D') with bounds (n - 1) and dl storage
    d : rank-1 array('D') with bounds (*)
    du : rank-1 array('D') with bounds (n - 1)
    x : rank-2 array('D') with bounds (*,*) and b storage
    info : int
    """
    pass

def zhbevd(ab, compute_v=None, lower=None, ldab=None, lrwork=None, liwork=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,info = zhbevd(ab,[compute_v,lower,ldab,lrwork,liwork,overwrite_ab])
    
    Wrapper for ``zhbevd``.
    
    Parameters
    ----------
    ab : input rank-2 array('D') with bounds (ldab,*)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    lrwork : input int, optional
        Default: (compute_v?1+5*n+2*n*n:n)
    liwork : input int, optional
        Default: (compute_v?3+5*n:1)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    z : rank-2 array('D') with bounds (ldz,ldz)
    info : int
    """
    pass

def zhbevx(ab, vl, vu, il, iu, ldab=None, compute_v=None, range=None, lower=None, abstol=None, mmax=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,m,ifail,info = zhbevx(ab,vl,vu,il,iu,[ldab,compute_v,range,lower,abstol,mmax,overwrite_ab])
    
    Wrapper for ``zhbevx``.
    
    Parameters
    ----------
    ab : input rank-2 array('D') with bounds (ldab,*)
    vl : input float
    vu : input float
    il : input int
    iu : input int
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    ldab : input int, optional
        Default: shape(ab,0)
    compute_v : input int, optional
        Default: 1
    range : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    abstol : input float, optional
        Default: 0.0
    mmax : input int, optional
        Default: (compute_v?(range==2?(iu-il+1):n):1)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    z : rank-2 array('D') with bounds (ldz,mmax)
    m : int
    ifail : rank-1 array('i') with bounds ((compute_v?n:1))
    info : int
    """
    pass

def zheev(a, compute_v=None, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,v,info = zheev(a,[compute_v,lower,lwork,overwrite_a])
    
    Wrapper for ``zheev``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 2*n-1
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    v : rank-2 array('D') with bounds (n,n) and a storage
    info : int
    """
    pass

def zheevd(a, compute_v=None, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,v,info = zheevd(a,[compute_v,lower,lwork,overwrite_a])
    
    Wrapper for ``zheevd``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: (compute_v?2*n+n*n:n+1)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    v : rank-2 array('D') with bounds (n,n) and a storage
    info : int
    """
    pass

def zheevr(a, jobz=None, range=None, uplo=None, il=None, iu=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,z,info = zheevr(a,[jobz,range,uplo,il,iu,lwork,overwrite_a])
    
    Wrapper for ``zheevr``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    jobz : input string(len=1), optional
        Default: 'V'
    range : input string(len=1), optional
        Default: 'A'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    il : input int, optional
        Default: 1
    iu : input int, optional
        Default: n
    lwork : input int, optional
        Default: 18*n
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    z : rank-2 array('D') with bounds (n,m)
    info : int
    """
    pass

def zhegv(a, b, itype=None, jobz=None, uplo=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,w,info = zhegv(a,b,[itype,jobz,uplo,overwrite_a,overwrite_b])
    
    Wrapper for ``zhegv``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (n,n)
    w : rank-1 array('d') with bounds (n)
    info : int
    """
    pass

def zhegvd(a, b, itype=None, jobz=None, uplo=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,w,info = zhegvd(a,b,[itype,jobz,uplo,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``zhegvd``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 2*n+n*n
    
    Returns
    -------
    a : rank-2 array('D') with bounds (n,n)
    w : rank-1 array('d') with bounds (n)
    info : int
    """
    pass

def zhegvx(a, b, iu, itype=None, jobz=None, uplo=None, il=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    w,z,ifail,info = zhegvx(a,b,iu,[itype,jobz,uplo,il,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``zhegvx``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,n)
    iu : input int
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    il : input int, optional
        Default: 1
    lwork : input int, optional
        Default: 18*n-1
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    z : rank-2 array('D') with bounds (n,m)
    ifail : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def zlange(norm, a): # real signature unknown; restored from __doc__
    """
    n2 = zlange(norm,a)
    
    Wrapper for ``zlange``.
    
    Parameters
    ----------
    norm : input string(len=1)
    a : input rank-2 array('D') with bounds (m,n)
    
    Returns
    -------
    n2 : float
    """
    pass

def zlarf(v, tau, c, work, side=None, incv=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = zlarf(v,tau,c,work,[side,incv,overwrite_c])
    
    Wrapper for ``zlarf``.
    
    Parameters
    ----------
    v : input rank-1 array('D') with bounds (*)
    tau : input complex
    c : input rank-2 array('D') with bounds (m,n)
    work : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    incv : input int, optional
        Default: 1
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (m,n)
    """
    pass

def zlarfg(n, alpha, x, incx=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    alpha,x,tau = zlarfg(n,alpha,x,[incx,overwrite_x])
    
    Wrapper for ``zlarfg``.
    
    Parameters
    ----------
    n : input int
    alpha : input complex
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    alpha : complex
    x : rank-1 array('D') with bounds (*)
    tau : complex
    """
    pass

def zlartg(f, g): # real signature unknown; restored from __doc__
    """
    cs,sn,r = zlartg(f,g)
    
    Wrapper for ``zlartg``.
    
    Parameters
    ----------
    f : input complex
    g : input complex
    
    Returns
    -------
    cs : float
    sn : complex
    r : complex
    """
    pass

def zlaswp(a, piv, k1=None, k2=None, off=None, inc=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = zlaswp(a,piv,[k1,k2,off,inc,overwrite_a])
    
    Wrapper for ``zlaswp``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (nrows,n)
    piv : input rank-1 array('i') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    k1 : input int, optional
        Default: 0
    k2 : input int, optional
        Default: len(piv)-1
    off : input int, optional
        Default: 0
    inc : input int, optional
        Default: 1
    
    Returns
    -------
    a : rank-2 array('D') with bounds (nrows,n)
    """
    pass

def zlauum(c, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    a,info = zlauum(c,[lower,overwrite_c])
    
    Wrapper for ``zlauum``.
    
    Parameters
    ----------
    c : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (n,n) and c storage
    info : int
    """
    pass

def zpbsv(ab, b, lower=None, ldab=None, overwrite_ab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    c,x,info = zpbsv(ab,b,[lower,ldab,overwrite_ab,overwrite_b])
    
    Wrapper for ``zpbsv``.
    
    Parameters
    ----------
    ab : input rank-2 array('D') with bounds (ldab,n)
    b : input rank-2 array('D') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (ldab,n) and ab storage
    x : rank-2 array('D') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def zpbtrf(ab, lower=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    c,info = zpbtrf(ab,[lower,ldab,overwrite_ab])
    
    Wrapper for ``zpbtrf``.
    
    Parameters
    ----------
    ab : input rank-2 array('D') with bounds (ldab,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    
    Returns
    -------
    c : rank-2 array('D') with bounds (ldab,n) and ab storage
    info : int
    """
    pass

def zpbtrs(ab, b, lower=None, ldab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = zpbtrs(ab,b,[lower,ldab,overwrite_b])
    
    Wrapper for ``zpbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('D') with bounds (ldab,n)
    b : input rank-2 array('D') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def zposv(a, b, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    c,x,info = zposv(a,b,[lower,overwrite_a,overwrite_b])
    
    Wrapper for ``zposv``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (n,n) and a storage
    x : rank-2 array('D') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def zpotrf(a, lower=None, clean=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,info = zpotrf(a,[lower,clean,overwrite_a])
    
    Wrapper for ``zpotrf``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    clean : input int, optional
        Default: 1
    
    Returns
    -------
    c : rank-2 array('D') with bounds (n,n) and a storage
    info : int
    """
    pass

def zpotri(c, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    inv_a,info = zpotri(c,[lower,overwrite_c])
    
    Wrapper for ``zpotri``.
    
    Parameters
    ----------
    c : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    inv_a : rank-2 array('D') with bounds (n,n) and c storage
    info : int
    """
    pass

def zpotrs(c, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = zpotrs(c,b,[lower,overwrite_b])
    
    Wrapper for ``zpotrs``.
    
    Parameters
    ----------
    c : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def zptsv(d, e, b, overwrite_d=None, overwrite_e=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    d,du,x,info = zptsv(d,e,b,[overwrite_d,overwrite_e,overwrite_b])
    
    Wrapper for ``zptsv``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (*)
    e : input rank-1 array('D') with bounds (n - 1)
    b : input rank-2 array('D') with bounds (*,*)
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    d : rank-1 array('d') with bounds (*)
    du : rank-1 array('D') with bounds (n - 1) and e storage
    x : rank-2 array('D') with bounds (*,*) and b storage
    info : int
    """
    pass

def zrot(x, y, c, s, n=None, offx=None, incx=None, offy=None, incy=None, overwrite_x=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    x,y = zrot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])
    
    Wrapper for ``zrot``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    y : input rank-1 array('D') with bounds (*)
    c : input float
    s : input complex
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 0
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('D') with bounds (*)
    y : rank-1 array('D') with bounds (*)
    """
    pass

def ztgsen(select, a, b, q, z, lwork=None, liwork=None, overwrite_a=None, overwrite_b=None, overwrite_q=None, overwrite_z=None): # real signature unknown; restored from __doc__
    """
    a,b,alpha,beta,q,z,m,pl,pr,dif,work,iwork,info = ztgsen(select,a,b,q,z,[lwork,liwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])
    
    Wrapper for ``ztgsen``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    a : input rank-2 array('D') with bounds (lda,*)
    b : input rank-2 array('D') with bounds (ldb,*)
    q : input rank-2 array('D') with bounds (ldq,*)
    z : input rank-2 array('D') with bounds (ldz,*)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    overwrite_z : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 2*m*(n-m)
    liwork : input int, optional
        Default: n+2
    
    Returns
    -------
    a : rank-2 array('D') with bounds (lda,*)
    b : rank-2 array('D') with bounds (ldb,*)
    alpha : rank-1 array('D') with bounds (n)
    beta : rank-1 array('D') with bounds (n)
    q : rank-2 array('D') with bounds (ldq,*)
    z : rank-2 array('D') with bounds (ldz,*)
    m : int
    pl : float
    pr : float
    dif : rank-1 array('d') with bounds (2)
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    iwork : rank-1 array('i') with bounds (MAX(1,liwork))
    info : int
    """
    pass

def ztrsyl(a, b, c, trana=None, tranb=None, isgn=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    x,scale,info = ztrsyl(a,b,c,[trana,tranb,isgn,overwrite_c])
    
    Wrapper for ``ztrsyl``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,m)
    b : input rank-2 array('D') with bounds (n,n)
    c : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    trana : input string(len=1), optional
        Default: 'N'
    tranb : input string(len=1), optional
        Default: 'N'
    isgn : input int, optional
        Default: 1
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (m,n) and c storage
    scale : float
    info : int
    """
    pass

def ztrtri(c, lower=None, unitdiag=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    inv_c,info = ztrtri(c,[lower,unitdiag,overwrite_c])
    
    Wrapper for ``ztrtri``.
    
    Parameters
    ----------
    c : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    
    Returns
    -------
    inv_c : rank-2 array('D') with bounds (n,n) and c storage
    info : int
    """
    pass

def ztrtrs(a, b, lower=None, trans=None, unitdiag=None, lda=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = ztrtrs(a,b,[lower,trans,unitdiag,lda,overwrite_b])
    
    Wrapper for ``ztrtrs``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (lda,n)
    b : input rank-2 array('D') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    lda : input int, optional
        Default: shape(a,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def zunghr(a, tau, lo=None, hi=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ht,info = zunghr(a,tau,[lo,hi,lwork,overwrite_a])
    
    Wrapper for ``zunghr``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    tau : input rank-1 array('D') with bounds (n - 1)
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: hi-lo
    
    Returns
    -------
    ht : rank-2 array('D') with bounds (n,n) and a storage
    info : int
    """
    pass

def zunghr_lwork(n, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    work,info = zunghr_lwork(n,[lo,hi])
    
    Wrapper for ``zunghr_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zungqr(a, tau, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    q,work,info = zungqr(a,tau,[lwork,overwrite_a])
    
    Wrapper for ``zungqr``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    tau : input rank-1 array('D') with bounds (k)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*n
    
    Returns
    -------
    q : rank-2 array('D') with bounds (m,n) and a storage
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def zungrq(a, tau, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    q,work,info = zungrq(a,tau,[lwork,overwrite_a])
    
    Wrapper for ``zungrq``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    tau : input rank-1 array('D') with bounds (k)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 3*m
    
    Returns
    -------
    q : rank-2 array('D') with bounds (m,n) and a storage
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def zunmqr(side, trans, a, tau, c, lwork, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    cq,work,info = zunmqr(side,trans,a,tau,c,lwork,[overwrite_c])
    
    Wrapper for ``zunmqr``.
    
    Parameters
    ----------
    side : input string(len=1)
    trans : input string(len=1)
    a : input rank-2 array('D') with bounds (lda,k)
    tau : input rank-1 array('D') with bounds (k)
    c : input rank-2 array('D') with bounds (ldc,n)
    lwork : input int
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    cq : rank-2 array('D') with bounds (ldc,n) and c storage
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

