import os
import numpy as np
import pytest
import matplotlib as mpl

mpl.use("Agg")
from mikeio import Dfsu, Mesh

##################################################
# these tests will not run if matplotlib is not installed
##################################################
pytest.importorskip("matplotlib")


def test_plot_bathymetry():
    filename = os.path.join("tests", "testdata", "oresund_sigma_z.dfsu")
    dfs = Dfsu(filename)
    dfs.plot()
    assert True


def test_plot_bathymetry_no_colorbar():
    filename = os.path.join("tests", "testdata", "oresund_sigma_z.dfsu")
    dfs = Dfsu(filename)
    dfs.plot(add_colorbar=False)
    assert True


def test_plot_2d():
    filename = os.path.join("tests", "testdata", "HD2D.dfsu")
    dfs = Dfsu(filename)
    dfs.plot(cmap="plasma")
    assert True


def test_plot_3d():
    filename = os.path.join("tests", "testdata", "oresund_sigma_z.dfsu")
    dfs = Dfsu(filename)
    dfs.plot()
    assert True


def test_plot_dfsu_contour():
    filename = os.path.join("tests", "testdata", "HD2D.dfsu")
    dfs = Dfsu(filename)
    dfs.plot(plot_type="contour", levels=5)
    assert True


def test_plot_dfsu_contourf_levels():
    filename = os.path.join("tests", "testdata", "HD2D.dfsu")
    dfs = Dfsu(filename)
    dfs.plot(plot_type="contourf", levels=[-3, -1])
    assert True


def test_plot_dfsu_contour_mixedmesh():
    filename = os.path.join("tests", "testdata", "FakeLake.dfsu")
    msh = Mesh(filename)
    msh.plot(plot_type="contour", levels=5)
    msh.plot(
        plot_type="contourf",
        title="contourf",
        show_mesh=False,
        levels=[-30, -24, -22, -10, -8],
    )
    assert True


def test_plot_dfsu_n_refinements():
    filename = os.path.join("tests", "testdata", "FakeLake.dfsu")
    msh = Mesh(filename)
    msh.plot(plot_type="contourf", levels=None, n_refinements=1)
    assert True


def test_plot_dfsu_shaded():
    filename = os.path.join("tests", "testdata", "HD2D.dfsu")
    dfs = Dfsu(filename)
    ds = dfs.read(items="Surface elevation", time_steps=0)
    elem40 = np.arange(40)
    wl_40 = ds.data[0][0, elem40]
    dfs.plot(wl_40, elements=elem40, plot_type="shaded", levels=5)
    assert True


def test_plot_dfsu():
    filename = os.path.join("tests", "testdata", "HD2D.dfsu")
    dfs = Dfsu(filename)
    data = dfs.read()
    dfs.plot(z=data[1][0, :], figsize=(3, 3), plot_type="mesh_only")
    assert True


def test_plot_dfsu_squeeze():
    filename = os.path.join("tests", "testdata", "HD2D.dfsu")
    dfs = Dfsu(filename)
    data = dfs.read(items=0, time_steps=0)
    dfs.plot(z=data)  # 1 item-dataset
    dfs.plot(z=data[0])  # 1 time-step-dataarray
    assert True


def test_plot_dfsu_arguments():
    filename = os.path.join("tests", "testdata", "NorthSea_HD_and_windspeed.dfsu")
    dfs = Dfsu(filename)
    data = dfs.read()
    dfs.plot(title="test", label="test", vmin=-23, vmax=23)
    assert True


def test_plot_mesh():
    filename = os.path.join("tests", "testdata", "odense_rough.mesh")
    msh = Mesh(filename)
    msh.plot(show_mesh=False)
    assert True


def test_plot_mesh_outline():
    filename = os.path.join("tests", "testdata", "odense_rough.mesh")
    msh = Mesh(filename)
    msh.plot(plot_type="outline_only")
    assert True
    msh.plot(plot_type=None)
    assert True


def test_plot_mesh_part():
    filename = os.path.join("tests", "testdata", "odense_rough.mesh")
    msh = Mesh(filename)
    msh.plot(elements=list(range(0, 100)))
    assert True


def test_plot_mesh_ax():
    import matplotlib.pyplot as plt

    filename = os.path.join("tests", "testdata", "odense_rough.mesh")
    msh = Mesh(filename)
    _, ax = plt.subplots()
    msh.plot(ax=ax)
    assert True


def test_plot_mesh_boundary_nodes():
    filename = os.path.join("tests", "testdata", "odense_rough.mesh")
    msh = Mesh(filename)
    msh.plot_boundary_nodes()
    msh.plot_boundary_nodes(["Land", "Sea"])
    assert True


def test_plot_invalid():
    filename = os.path.join("tests", "testdata", "odense_rough.mesh")
    mesh = Mesh(filename)
    with pytest.raises(Exception):
        mesh.plot(plot_type="invalid")
    with pytest.raises(Exception):
        mesh.plot(plot_type="invalid")


def test_plot_dfsu_vertical_profile():
    import matplotlib.pyplot as plt

    filename = os.path.join("tests", "testdata", "oresund_vertical_slice.dfsu")
    dfs = Dfsu(filename)
    time_step = 1
    item_number = 1
    data = dfs.read()[item_number].to_numpy()[time_step, :]
    # defaults
    dfs.plot_vertical_profile(data)
    dfs.plot_vertical_profile(data, time_step, 0, 20)
    dfs.plot_vertical_profile(
        data,
        title="txt",
        label="txt",
        edge_color="0.3",
        cmin=0,
        cmax=20,
        cmap="plasma",
        figsize=(2, 2),
    )
    _, ax = plt.subplots()
    dfs.plot_vertical_profile(data, ax=ax)
    assert True
