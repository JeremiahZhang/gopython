# 全加器真值表计算

def func(ai, bi, ci_1):
	y1 = (ai and (not bi)) or ((not ai) and bi)
	si = (y1 and (not ci_1)) or ((not y1) and ci_1)

	inter_1 = (ai and bi)
	inter_2 = (y1 and ci_1)

	ci = inter_1 or inter_2

	return(si, ci)
