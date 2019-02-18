from django.shortcuts import render, redirect
from .forms import CalcForm
from .models import Nums
import plotly
import plotly.graph_objs as go


def overview(request):
    nums = 0

    if request.method == 'POST':
        form = CalcForm(request.POST)
        nums2 = request.POST.get('nums')
        nums2 = nums2.split(",")
        nums2 = list(map(int, nums2))
        max_nums = calculate_maxmimum(nums2)
        sum_nums = calculate_sum(nums2)
        mean_nums = calculate_mean(nums2)
        var_nums = calculate_variance(nums2)
        sd_nums = calculate_standard_deviation(nums2)
        boxplot_nums = boxplot(nums2)

        return render(request, 'calculations/calc_overview.html', {
            'nums2': nums2,
            'max_nums': max_nums,
            'sum_nums': sum_nums,
            'mean_nums': mean_nums,
            'var_nums': var_nums,
            'sd_nums': sd_nums,
            'boxplot_nums': boxplot_nums,
        })
    else:
        nums = CalcForm()

    return render(request, 'calculations/calc_overview.html', {})


def calculate_maxmimum(x):
    max = x[0]
    for i in x[1:]:
        if i > max:
            max = i

    return max


def calculate_sum(x):
    sum = 0
    for i in x:
        sum += i

    return sum


def calculate_mean(x):
    sum = calculate_sum(x)
    n = get_len(x)

    return sum / n


def calculate_variance(x):
    mean = calculate_mean(x)
    square = ((i - mean) ** 2 for i in x)
    sum_of_squares = calculate_sum(square)

    return sum_of_squares / get_len(x)


def calculate_standard_deviation(x):
    return calculate_variance(x) ** (1 / 2)


def get_len(x):
    n = 0
    for i in x:
        n += 1

    return n


def boxplot(x):
    y = plotly.offline.plot({
        "data": [go.Box(x = x)],
        "layout": go.Layout(title = "Boxplot number input",
                            showlegend = False)
    }, auto_open = False, output_type = 'div', include_plotlyjs = False)

    return y
