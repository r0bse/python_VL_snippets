import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D


def radar_factory(num_vars, frame='circle'):
    """Create a radar chart with `num_vars` axes.

    This function creates a RadarAxes projection and registers it.

    Parameters
    ----------
    num_vars : int
        Number of variables for radar chart.
    frame : {'circle' | 'polygon'}
        Shape of frame surrounding axes.

    """
    # calculate evenly-spaced axis angles
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)

    class RadarTransform(PolarAxes.PolarTransform):
        def transform_path_non_affine(self, path):
            # Paths with non-unit interpolation steps correspond to gridlines,
            # in which case we force interpolation (to defeat PolarTransform's
            # autoconversion to circular arcs).
            if path._interpolation_steps > 1:
                path = path.interpolated(num_vars)
            return Path(self.transform(path.vertices), path.codes)

    class RadarAxes(PolarAxes):

        name = 'radar'

        PolarTransform = RadarTransform

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # rotate plot such that the first axis is at the top
            self.set_theta_zero_location('N')

        def fill(self, *args, closed=True, **kwargs):
            """Override fill so that line is closed by default"""
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """Override plot so that line is closed by default"""
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)

        def _gen_axes_patch(self):
            # The Axes patch must be centered at (0.5, 0.5) and of radius 0.5
            # in axes coordinates.
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                return RegularPolygon((0.5, 0.5), num_vars,
                                      radius=.5, edgecolor="k")
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

        def draw(self, renderer):
            """ Draw. If frame is polygon, make gridlines polygon-shaped """
            if frame == 'polygon':
                gridlines = self.yaxis.get_gridlines()
                for gl in gridlines:
                    gl.get_path()._interpolation_steps = num_vars
            super().draw(renderer)


        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                # spine_type must be 'left'/'right'/'top'/'bottom'/'circle'.
                spine = Spine(axes=self,
                              spine_type='circle',
                              path=Path.unit_regular_polygon(num_vars))
                # unit_regular_polygon gives a polygon of radius 1 centered at
                # (0, 0) but we want a polygon of radius 0.5 centered at (0.5,
                # 0.5) in axes coordinates.
                spine.set_transform(Affine2D().scale(.5).translate(.5, .5)
                                    + self.transAxes)


                return {'polar': spine}
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)
    return theta

if __name__=="__main__":

    covid_data = pd.read_csv('flask/static/covid_berlin.csv',
                             sep=';',
                             decimal=',',
                             quotechar="'",
                             encoding="UTF-8")

    # parse datetime
    covid_data['datum'] = pd.to_datetime(covid_data['datum'])
    # parse to specific type
    covid_data['rel_veraenderung_der_7_tage_inzidenz'] = covid_data['rel_veraenderung_der_7_tage_inzidenz'].astype(float)
    # drop a column
    covid_data.drop('id', axis=1, inplace=True)

    # manipulate column data
    covid_data["todesfaelle"] = [ value/1000 for value in covid_data["todesfaelle"]]
    covid_data["neue_faelle"] = [ value/1000 for value in covid_data["neue_faelle"]]
    covid_data["genesene"] = [ value/100000 for value in covid_data["genesene"]]
    covid_data["fallzahl"] = [ value/100000 for value in covid_data["fallzahl"]]

    covid_data = covid_data.query('datum == "2022-08-17" | datum == "2021-08-17"')

    #drop unneeded data
    covid_data.drop('datum', axis=1, inplace=True)
    covid_data.drop('rel_veraenderung_der_7_tage_inzidenz', axis=1, inplace=True)
    covid_data.drop('7_tage_inzidenz', axis=1, inplace=True)

    # data_to_show = covid_data[["neue_faelle", "genesene", "todesfaelle"]]

    N = len(covid_data.columns)
    theta = radar_factory(N, frame='polygon')

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='radar'))
    ax.set_title("Radar Chart Example",  position=(0.5, 1.1), ha='center')

    for d in covid_data.values:
        print(d)
        line = ax.plot(theta, d)
        ax.fill(theta, d, alpha=0.25, label='_nolegend_')
    ax.set_varlabels(covid_data.columns)

    plt.show()