from pymatgen.ext.matproj import MPRester # MPRestError
from mp_api.client.core.client import MPRestError
from pymatgen.electronic_structure.plotter import BSPlotter

API_KEY = "tU0vSHipjvPtj98ZC7OpIaFvgPo6Fd8t" # "Rm5KndBPg1E8Tanuv9qL"

# Import band structure
mpid = "mp-684555" # SnSe

try:
    mp = MPRester(API_KEY)
    bs = mp.get_bandstructure_by_material_id(mpid)
    if bs is None:
        raise MPRestError
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    print(ex.args[0])
    message = template.format(type(ex).__name__, ex.args)
    print(message)

else:
    with MPRester(API_KEY) as mp:
        bs = mp.get_bandstructure_by_material_id(mpid)
finally:
    mp.__exit__(None, None, None)


print(mp)

bs_plot = BSPlotter(bs)
bs_plot.get_plot().show()





