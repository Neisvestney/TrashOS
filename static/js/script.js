var app, map;
var scripts = document.getElementsByTagName("script"),
    src = scripts[scripts.length - 1].src.split('/').reverse().slice(2).reverse().join('/');

console.log(src)

$(document).ready(function () {
    $('.inner').animate({
        height: "90%"
    }, 1500);

    if ($("#map").length) {
        let el = "#map"
        if ($(".panel").length) el = ".panel"

        app = new Vue({
            el: el,
            data: {
                trashes: {},
                icons: []
            },
            watch: {
                trashes: function (value) {
                    for (i in value) {
                        this.icons[i]._data.trash = value[i]
                    }
                }
            }
        });
        DG.then(function () {

            map = DG.map('map', {
                center: [45.023743, 38.96785],
                zoom: 50
            });

            $.get('/api/trashes/', function (data) {
                app.trashes = data.trashes;

                for (let i in app.trashes) {
                    let IconClass = Vue.extend({
                        //template: `<div><img src="${src}/img/point.svg" alt=""><div class="fullness-panel">sd</div></div>`,
                        template: `<div class="point">
                                        <img src="${src}/img/point.svg" alt="">
                                        <div class="fullness-panel">
                                            <img src="${src}/img/fullnessindicator.svg" alt="" v-bind:style="{ top: (1 - trash.fullness) * 100 + '%' }">
                                            <p class="title">{{ trash.address }}</p>
                                            <p class="percent">{{ trash.fullness*100 }}%</p>
                                        </div>
                                    </div>`,
                        data: function () {
                            return {
                                trash: app.trashes[i]
                            }
                        }
                    })
                    let iconClass = new IconClass();
                    app.icons.push(iconClass);
                    iconClass.$mount();

                    let icon = DG.divIcon({
                        iconSize: [26, 31],
                        html: `<div id='trash-${i}'></div>`
                    });

                    DG.marker([ app.trashes[i].x,  app.trashes[i].y], {
                        icon: icon
                    }).addTo(map);

                    $('#trash-' + i).append(iconClass.$el);
                }
            })

            setInterval(function () {
                $.get('/api/trashes/', function (data) {
                    app.trashes = data.trashes;
                })
            }, 2000)

            DG.control.location({position: 'bottomright'}).addTo(map);
            DG.control.scale().addTo(map);
        });
    }
})