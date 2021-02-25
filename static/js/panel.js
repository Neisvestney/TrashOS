DG.then(function () {
    var map,
        myIcon,
        myDivIcon;

    map = DG.map('map', {
        center: [54.98, 82.89],
        zoom: 13
    });

    myIcon = DG.icon({
        iconUrl: 'https://maps.api.2gis.ru/2.0/example_logo.png',
        iconSize: [48, 48]
    });
    DG.marker([54.98, 82.89], {
        icon: myIcon
    }).addTo(map);

    myDivIcon = DG.divIcon({
        iconSize: [70, 20],
        html: '<b style="color:blue;">HTML-код</b>'
    });
    DG.marker([54.98, 82.87], {
        icon: myDivIcon
    }).addTo(map);

    DG.control.location({position: 'bottomright'}).addTo(map);
    DG.control.scale().addTo(map);
});