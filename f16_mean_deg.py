import numpy as np
import warnings

def mean_deg(a):
    """takes an list of angle values in degrees and returns the averaged value"""
    
    #a = np.round( np.random.rand(4)*360 )
    # a = [270,270]
    # print(a)
    
    if len(a)==0:
        aa=np.nan
    elif all(np.isnan(a)):
        aa=np.nan
    else:
        x = np.cos(np.radians(a))
        y = np.sin(np.radians(a))
         
        csx = np.nancumsum( x )
        csy = np.nancumsum( y )
       
        # mean angle is either 0, 90, 180 or 270 deg
        if   csx[-1]> 0 and csy[-1]==0:  # 0
                                            aa =   0
        elif csx[-1]==0 and csy[-1]> 0:  # 90
                                            aa =  90
        elif csx[-1]< 0 and csy[-1]==0:  # 180
                                            aa = 180
        elif csx[-1]==0 and csy[-1]< 0:  # 270
                                            aa = 270
        else:
                                            aa = np.rad2deg(np.arctan ( csy[-1] / csx[-1] ))
        
        # mean angle is in one of the 4 quarters of the circle
        if   csx[-1]> 0 and csy[-1]> 0:  # Q1
                                            aa = aa
        elif csx[-1]< 0 and csy[-1]> 0:  # Q2
                                            aa = aa+180
        elif csx[-1]< 0 and csy[-1]< 0:  # Q3
                                            aa = aa+180
        elif csx[-1]> 0 and csy[-1]< 0:  # Q4
                                            aa = aa+360
    
    return aa
    
    # print(aa)
    
    # import matplotlib as plt
    # fig, ax = plt.pyplot.subplots()
    # plt.pyplot.plot( [ 0,  0], [-2,  2 ], color='black', linewidth=0.5)
    # plt.pyplot.plot( [-2,  2], [ 0,  0 ], color='black', linewidth=0.5)
    # plt.pyplot.title(np.round(aa))
    
    # col = plt.pyplot.get_cmap('tab10')
    # col = [plt.colors.to_rgba(c) for c in col(np.arange(col.N))]
    
    # for i in range(len(a)):
    #     arrow = plt.patches.FancyArrowPatch(posA=(0, 0), posB=(x[i],y[i]),\
    #                                         arrowstyle='->', mutation_scale=15,\
    #                                         color=col[i],linewidth=1)
    #     plt.pyplot.gca().add_patch(arrow)
    #     if i>0:
    #         arrow = plt.patches.FancyArrowPatch(posA=(csx[i-1], csy[i-1]), posB=(csx[i],csy[i]),\
    #                                             arrowstyle='->', mutation_scale=15,\
    #                                             color=col[i],linewidth=0.5)
    #         plt.pyplot.gca().add_patch(arrow)
    #     arrow = plt.patches.FancyArrowPatch(posA=(0, 0), posB=(csx[-1],csy[-1]),\
    #                                         arrowstyle='->', mutation_scale=15,\
    #                                         color='black',linewidth=2)
    #     plt.pyplot.gca().add_patch(arrow)
    # del arrow
    # ax.set_aspect('equal')
    # ax.set_title(np.round(aa))
    # ax.grid(True)
    
    
    # L = np.ceil( np.max(np.abs(np.concatenate((csx, csy), axis=0))) )
    # ax.set_xlim(-L, L)
    # ax.set_ylim(-L, L)
    
    # plt.pyplot.savefig('plot.pdf', format='pdf')
    
def warning_handler(message, *args, **kwargs):
    print(f"Warning caught: {message}")
    print(f"Arguments that caused the warning: {args}")

# Wrapper function to catch warnings
def mean_deg_w(a):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")  # Ensure all warnings are caught
        try:
            # Call the function
            result = mean_deg(a)
        except Exception as e:
            print(f"Exception caught: {e}")
        # Check if any warnings were raised
        if w:
            for warning in w:
                warning_handler(warning.message, a)
        return result
    
    
