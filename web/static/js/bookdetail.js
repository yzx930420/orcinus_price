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
                    return Highcharts.dateFormat('%m-%d', this.value);
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
    isbn = $("#isbn").attr("isbn")
    $.post(
       "/json/price/"+isbn,{},function(ret){

            for(var i = 0; i < ret.length; i++){
                charts.addSeries({
                    name:ret[i].name,
                    data:(function () {
                        var data = [];
                        for(var j = 0; j < ret[i].data.length; j++){
                            data.push(ret[i].data[j].price);
                        }
                        return data;
                    })(),
                    pointStart: new Date().setMonth(new Date().getMonth() - 1),
                    pointInterval: 24 * 3600 * 1000
                }, true, false);
            }
        },"json"
    )
}