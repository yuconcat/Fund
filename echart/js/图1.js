(function () {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('one'));   //此及以上都是固定的

    myChart.setOption({
        series : [
            {
                name: '访问来源',
                type: 'pie',
                radius: '55%',
                data:[
                    {value:235, name:'视频广告'},
                    {value:274, name:'联盟广告'},
                    {value:310, name:'邮件营销'},
                    {value:335, name:'直接访问'},
                    {value:400, name:'搜索引擎'}
                ]
            }
        ]
    })

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);        //这个也是固定的

    //设置图表随盒子变化而变化
    window.addEventListener("resize",function () { myChart.resize() });
})();

