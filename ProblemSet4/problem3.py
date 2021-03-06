# Problem Set 4, Problem 3
#
# READ problem3.md

import pylab, numpy as np

from ProblemSet4 import r_squared, Climate, generate_models, FILE_PATH, INTERVAL_1

def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-square for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points
    Args:
        x: a list of length N, representing the x-coords of N sample points
        y: a list of length N, representing the y-coords of N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a numpy array storing the coefficients of
            a polynomial.
    Returns:
        None
    """
    pylab.plot(x, y, '.b', label='Measured data')
    pylab.xlabel('Year')
    pylab.ylabel('Temperature [degC]')

    rSquared = []
    for model in models:
        estimated = np.polyval(model, x)
        rSquared.append(r_squared(y, estimated))
        pylab.plot(x, estimated, 'r', label= 'Estimated model')


    pylab.title('Estimated model with c1 = %.3f ' % models[0][0] + 'and c2 = %.3f' % models[0][1] + ' and R^2 = %.3f' % rSquared[0])
    pylab.legend(loc='upper right')
    pylab.show()

def main():
    raw_data = Climate(FILE_PATH)

    y = []
    x = INTERVAL_1
    for year in INTERVAL_1:
        y.append(raw_data.get_daily_temp('BOSTON', 1, 10, year))
    models = generate_models(x, y, [1])
    evaluate_models_on_training(x, y, models)

if __name__ == '__main__':
    main()