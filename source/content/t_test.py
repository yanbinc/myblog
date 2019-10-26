est_vari_model_err=SS_error/dF_error
SE_i=(est_vari_model_err*np.diag(np.linalg.pinv(mat_X.T*mat_X)))**0.5
# the standard error of regression
t_stat_i=B/SE_i
print (SE_i)
print (t_stat_i)
