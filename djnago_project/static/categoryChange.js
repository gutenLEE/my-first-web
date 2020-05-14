

 function categoryChange(elementId) {
    alert(document.getElementById("city_select").value);

    var seoul = ["종로구", "중구", "용산구", "성동구", "광진구", "동대문구", "중랑구", "성북구",
                 "강북구", "도봉구", "노원구", "은평구", "서대문구", "마포구", "양천구", "강서구",
                 "구로구", "금천구", "영등포구", "동작구", "관악구", "서초구", "강남구", "송파구", "강동구"]

    var select = document.getElementById(elementId);
    var city = document.getElementById("city_select").value;

    if( city == "서울특별시") var d = seoul;

    for (x in d){
        var opt = document.createElement('option');
        opt.value = d[x];
        opt.innerHTML = d[x];
        select.appendChild(opt);
    }
 };

 function category_dong(elementId) {
    alert(document.getElementById("gu_select").value);


    var jong_gu = ["소공동", "회현동", "명동", "필동", "장충동" ,
                   "광희동", "을지로동", "신당동", "다산동", "약수동",
                   "청구동", "신당제5동", "동화동", "황학동", "중림동"]


    var jong_ro_gu = ["청운효자동", "사직동", "삼청동", "부암동", "평창동",
                      "무악동", "교남동", "가회동", "종로1.2.3.4가동", "종로5.6가동",
                       "이화동", "혜화동", "창신제1동", "창신제2동", "창신제3동",
                       "숭인제1동", "숭인제2동"]

    var select = document.getElementById(elementId);
    var city = document.getElementById("gu_select").value;

    if( city == "중구") var d = jong_gu;

    for (x in d){
        var opt = document.createElement('option');
        opt.value = d[x];
        opt.innerHTML = d[x];
        select.appendChild(opt);
    }
 };
