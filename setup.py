from setuptools import setup
from glob import glob

data_sets = [
    "De-noised_100G_3T_300cPerT_dynamics_8_DS8",
    "De-noised_100G_3T_300cPerT_dynamics_9_DS4",
    "De-noised_100G_4T_300cPerT_dynamics_10_DS5",
    "De-noised_100G_6T_300cPerT_dynamics_7_DS6",
    "De-noised_100G_7T_300cPerT_dynamics_11_DS7",
    "De-noised_100G_9T_300cPerT_4_DS1",
    "De-noised_1200G_9T_300cPerT_6_DS3",
    "De-noised_400G_9T_300cPerT_5_DS2",
]

setup(
    name="SERGIO",
    version="1.0.0",
    url="https://github.com/gitHBDX/SERGIO.git",
    author="Payam Dibaeinia",
    description="SERGIO is a simulator for single-cell expression data guided by gene regulatory networks.",
    packages=["SERGIO"],
    include_package_data=True,
    data_files=[(f"sergio_data_sets/{d}", glob(f"data_sets/{d}/*")) for d in data_sets],
    install_requires=["numpy >= 1.13.3", "scipy >= 1.1.0", "networkx >= 2.0"],
)
