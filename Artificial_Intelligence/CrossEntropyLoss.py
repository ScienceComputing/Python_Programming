from sklearn.metrics import log_loss
log_loss(["ginger", "rose", "rose", "ginger"], [[.1, .9], [.8, .2], [.9, .1], [.05, .95]])
# 2.3025850929940455

log_loss(["spam", "ham", "ham", "spam"], [[.1, .9], [.8, .2], [.9, .1], [.05, .95]])
# 0.1212894692543532 # TD ?
