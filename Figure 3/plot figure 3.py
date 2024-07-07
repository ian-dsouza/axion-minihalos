import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset
import os


# Note: Alhtough the zoomed plot may not be correctly positioned within the overall figure when the figure pops up, when you save the figure, it will be correctly positioned .

# PARAMETERS
save_to_disk = True # If set to True, figure will be saved to disk. Set to false if you don't want figure to be saved to disk.




# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the working directory to the script's directory
os.chdir(script_dir)

# Load numerical simulation data points: provided to us courtesy of Jacob Shen from the S2023 paper.
data_c_10 = np.genfromtxt(os.path.join('..', 'Data', 'S2023 Fig 3, c=10.dat'), dtype=None, delimiter='') 
data_c_30 = np.genfromtxt(os.path.join('..', 'Data', 'S2023 Fig 3, c=30.dat'), dtype=None, delimiter='')
data_c_100 = np.genfromtxt(os.path.join('..', 'Data', 'S2023 Fig 3, c=100.dat'), dtype=None, delimiter='')

# Load E_frac array
E_fracs = np.load(r"E_fracs.npy")

# Load the survival fractions computed using the sequential stripping model without relaxation 
survival_fractions_c_10 = np.load(r"survival_fractions_c_10_sequential_stripping.npy")
survival_fractions_c_30 = np.load(r"survival_fractions_c_30_sequential_stripping.npy")
survival_fractions_c_100 = np.load(r"survival_fractions_c_100_sequential_stripping.npy")
survival_fractions_c_500 = np.load(r"survival_fractions_c_500_sequential_stripping.npy")

# Load the survival fractions computed using the S2023 semi-analytical fitting functions
survival_fractions_S2023_fitting_fn_c_10 = np.load(os.path.join('..', 'Data', "survival_fractions_S2023_fittingfn_c_10.npy"))
survival_fractions_S2023_fitting_fn_c_30 = np.load(os.path.join('..', 'Data', "survival_fractions_S2023_fittingfn_c_30.npy"))
survival_fractions_S2023_fitting_fn_c_100 = np.load(os.path.join('..', 'Data', "survival_fractions_S2023_fittingfn_c_100.npy"))
survival_fractions_S2023_fitting_fn_c_500 = np.load(os.path.join('..', 'Data', "survival_fractions_S2023_fittingfn_c_500.npy"))

plt.rcParams["mathtext.fontset"] = "cm"


fig, ax = plt.subplots(1, figsize=(10,6))
fig.subplots_adjust(left=0.2, bottom=0.2)

ax.loglog(E_fracs, survival_fractions_c_10, color="green", label=r"$c=10$")
ax.loglog(E_fracs, survival_fractions_c_30, color="red", label=r"$c=30$")
ax.loglog(E_fracs, survival_fractions_c_100, color="blue", label=r"$c=100$")
ax.loglog(E_fracs, survival_fractions_c_500, color="orange", label=r"$c=500$")
ax.loglog([], [], color="black", label="Sequential Stripping")

ax.scatter(data_c_10[:,0], data_c_10[:,1], 80*np.ones(np.size(data_c_10[:,0])), color="green", marker="o")
ax.scatter(data_c_30[:,0], data_c_30[:,1], 80*np.ones(np.size(data_c_30[:,0])), color="red", marker="o")
ax.scatter(data_c_100[:,0], data_c_100[:,1], 80*np.ones(np.size(data_c_100[:,0])), color="blue", marker="o")
ax.scatter([], [], color="black", label=r"S2023's simulation")


ax.loglog(E_fracs, survival_fractions_S2023_fitting_fn_c_10, color="green", linestyle="dashed")
ax.loglog(E_fracs, survival_fractions_S2023_fitting_fn_c_30, color="red", linestyle="dashed")
ax.loglog(E_fracs, survival_fractions_S2023_fitting_fn_c_100, color="blue", linestyle="dashed")
ax.loglog(E_fracs, survival_fractions_S2023_fitting_fn_c_500, color="orange", linestyle="dashed")
plt.loglog([], [], color="black", linestyle="dashed", label="S2023's fitting function")

# # Setup zoom window
axins = zoomed_inset_axes(ax, 1.5, loc="lower left", bbox_to_anchor=(140,80), borderpad=3)
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.6")
axins.set_xlim([1e-2,40])
axins.set_ylim([0.2,1.1])

# # Plot zoom window
axins.loglog(E_fracs, survival_fractions_c_10, color="green", label=r"$c=10$")
axins.loglog(E_fracs, survival_fractions_c_30, color="red", label=r"$c=30$")
axins.loglog(E_fracs, survival_fractions_c_100, color="blue", label=r"$c=100$")
axins.loglog(E_fracs, survival_fractions_c_500, color="orange", label=r"$c=500$")

axins.scatter(data_c_10[:,0], data_c_10[:,1], 80*np.ones(np.size(data_c_10[:,0])), color="green", marker="o")
axins.scatter(data_c_30[:,0], data_c_30[:,1], 80*np.ones(np.size(data_c_30[:,0])), color="red", marker="o")
axins.scatter(data_c_100[:,0], data_c_100[:,1], 80*np.ones(np.size(data_c_100[:,0])), color="blue", marker="o")


axins.loglog(E_fracs, survival_fractions_S2023_fitting_fn_c_10, color="green", linestyle="dashed")
axins.loglog(E_fracs, survival_fractions_S2023_fitting_fn_c_30, color="red", linestyle="dashed")
axins.loglog(E_fracs, survival_fractions_S2023_fitting_fn_c_100, color="blue", linestyle="dashed")
axins.loglog(E_fracs, survival_fractions_S2023_fitting_fn_c_500, color="orange", linestyle="dashed")

axins.set_yticks([0.2, 0.3, 0.4, 0.6, 1])
axins.set_yticklabels(["0.2", "0.3", "0.4", "0.6", "1"])

ax.tick_params(which="both", labelright=True, right=True)
axins.tick_params(which="both", labelright=True, right=True)
ax.set_xlabel(r"$E_{\rm frac}$", fontsize=18)
ax.set_ylabel(r"$1 - \frac{\Delta M}{M_{\rm vir}}$", fontsize=18)
# ax.set_title(r"Survival fraction vs. $E_{\mathrm{frac}}$", fontsize=18)
ax.set_xlim(1e-4, 1e3)
ax.legend(ncol=2, loc="lower left", bbox_to_anchor=(0.6,0.89), fontsize = 10)

if save_to_disk:
    fig.savefig("Figure 3.pdf")

plt.show()