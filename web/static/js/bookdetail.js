/**
 * Created by Administrator on 14-4-21.
 */
$(function () {

    Highcharts.setOptions({
        global: {
            useUTC: false
        }
    });

    $('#price_trend').highcharts({
        chart: {
            type: 'spline',
            animation: Highcharts.svg,
            events: {
                load: function () {
                    // ajax请求数据
                    getData();
                }
            }
        },

        title: {
            text: ''
        },

        xAxis: {
            type: 'datetime',
            tickPixelInterval: 120,
            labels: {
                formatter: function () {
                    return  Highcharts.dateFormat('%m-%d', this.value);
                }
            }
        },
        yAxis: {
            title: {
                text: ''
            },

            plotLines: [
                {
                    value: 0,
                    width: 1,
                    color: '#808080'
                }
            ]
        },
        tooltip: {
            formatter: function () {
                return '<b>' + this.series.name + '</b><br/>' +
                    '日期:  ' + Highcharts.dateFormat('%y-%m-%d', this.x) + '<br/>' +
                    '价格:  ￥' + Highcharts.numberFormat(this.y, 2);
            }
        },
        legend: {
            enabled:true
        },
        exporting: {
            enabled: false
        }
    });
});

function getData() {
    var charts = $('#price_trend').highcharts();
    var series = charts.series;
    var i;
    while (series.length > 0) {
        series[0].remove();
    }
    var arr = ["京东商城", "当当网"];
    for (i = 0; i < 2; i++) {
        charts.addSeries({
            name: arr[i],
            data: (function () {
                var data = [], i;

                for (i = 1; i <= 30; i++) {
                    data.push(Math.random() * 50 + 30);
                }
                return data;
            })(),
            pointStart: new Date().setMonth(new Date().getMonth() - 1),
            pointInterval: 24 * 3600 * 1000
        }, true, false);
    }
}