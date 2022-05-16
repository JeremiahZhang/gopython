# 2线-4线译码器

def func(a0, a1):
    y3_ = not((a0 and a1))
    y2_ = not((a0 and (not a1)))
    y1_ = not((not a0) and a1)
    y0_ = not((not a0) and (not a1))
    print(y3_, y2_, y1_, y0_)
    return(y3_, y2_, y1_, y0_)

Y3_, Y2_, Y1_, Y0_ = func(0, 0)