# Graf rychlosti v51 a detail kolem zvoleného úhlu.
# Instalace knihoven: python -m pip install numpy matplotlib
# Spuštění: python3 graf.py
# PDF se uloží do složky aktuálního adresáře

import numpy as np                 # výpočty s čísly a vektory
import matplotlib.pyplot as plt    # vykreslování grafů

# Vstupní hodnoty
h  = 9         # [m]
r2 = 6         # [m]
l  = 18        # [m]
PHI2 = 30      # [deg], úhel pro kontrolu
omega21 = 1.2  # [rad/s]
filename = "v51"

# Výčíslení rychlosti
phi2 = np.linspace(0, 2 * np.pi, 2001) # [rad], [0, ..., 2pi]
phi2_deg = np.deg2rad(PHI2)

v51 = l*r2*(r2 + h*np.cos(phi2)) / (h*h + 2*h*r2*np.cos(phi2) + r2*r2) * omega21

# Vykreslení celého grafu
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 14,
})

fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(phi2, v51, color="black", linewidth=2)
ax.axvline(phi2_deg, color="red", linestyle="--", linewidth=2)
ax.grid(True)
ax.set_xlim(-0.1, 2 * np.pi + 0.1)

ax.set_xlabel(r"$\varphi_2\;[\mathrm{rad}]$")
ax.set_ylabel(r"$v_{51}\;[\mathrm{m}\cdot\mathrm{s}^{-1}]$")
ax.ticklabel_format(axis="both", style="plain", useOffset=False, useMathText=True)

fig.tight_layout()
fig.savefig(filename + ".pdf")

# Detail kolem PHI2
x_min = np.deg2rad(PHI2 - 10)
x_max = np.deg2rad(PHI2 + 10)

idx = (phi2 >= x_min) & (phi2 <= x_max)
y_min = np.min(v51[idx])
y_max = np.max(v51[idx])

ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

fig.set_size_inches(3, 3)
fig.tight_layout()
fig.savefig(filename + "_detail.pdf")

plt.show()