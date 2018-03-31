var d = document,
    $one  = d.getElementById('content-one'),
    $two = d.getElementById('content-two'),
    $three = d.getElementById('content-three'),
    $four = d.getElementById('content-four'),

    oneH  = $one.offsetHeight;
    twoH = ($one.offsetHeight + $two.offsetHeight);
    threeH = ($one.offsetHeight + $two.offsetHeight + $three.offsetHeight);

$two.innerHTML = $one.innerHTML +'<p style="height:'+ oneH +'px;" />';
$two.scrollTop = oneH;

$three.innerHTML = $one.innerHTML +'<p style="height:'+ oneH +'px;" />';
$three.scrollTop = twoH;

$four.innerHTML = $one.innerHTML +'<p style="height:'+ oneH +'px;" />';
$four.scrollTop = threeH;
