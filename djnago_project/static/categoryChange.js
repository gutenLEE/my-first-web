    var addr = {{ addre|safe }};
    var gu_list = []
    var dong_list = []

    function categoryChange(elementId) {

        alert(document.getElementById("city_select").value);
        var selected_city = document.getElementById("city_select").value

        var target = document.getElementById(elementId);

        for(var i=0; i < addr.length; i++) {

	        //선택된 1단계 구역의 행정동 리스트
	        var city_check = addr[i][0];
	        if( city_check.indexOf(selected_city) != -1){

	                // 1단계만 존재하는 구역 pass
	            if( addr[i][1] == ""){
	            }
	            else{
                    if (gu_list.indexOf(addr[i][1]) == -1){
                        gu_list.push(addr[i][1]);
                        console.log(gu_list);
                    }
                }
	        }
        };
            // to create select options
        for (i = 0; i < gu_list.length; i++){
            var opt = document.createElement('option');
            opt.value = gu_list[i];
            opt.innerHTML = gu_list[i];
            target.appendChild(opt);
        }
    };

    function category_dong(elementId) {
        alert(document.getElementById("gu_select").value);

        var target = document.getElementById(elementId);
        var selected_gu = document.getElementById("gu_select").value;
        var selected_city = document.getElementById("city_select").value
        console.log(selected_city)


       for(var i=0; i < addr.length; i++) {

            if ( addr[i][0] == selected_city && addr[i][1] == selected_gu){

                if( addr[i][2] == ""){
	            }
	            else{
                    if (dong_list.indexOf(addr[i][2]) == -1){
                        dong_list.push(addr[i][2]);
                    };
                }
            };
       };

       console.log(dong_list)

        // to create select options
        for (i = 0; i < dong_list.length; i++){
                var opt = document.createElement('option');
                opt.value = dong_list[i];
                opt.innerHTML = dong_list[i];
                target.appendChild(opt);
        };
};


    function printClock() {

        var clock = document.getElementById("clock");            // 출력할 장소 선택
        var currentDate = new Date();                                     // 현재시간
        var calendar = currentDate.getFullYear() + "-" + (currentDate.getMonth()+1) + "-" + currentDate.getDate() // 현재 날짜
        var amPm = 'AM'; // 초기값 AM
        var currentHours = addZeros(currentDate.getHours(),2);
        var currentMinute = addZeros(currentDate.getMinutes() ,2);
        var currentSeconds =  addZeros(currentDate.getSeconds(),2);

        if(currentHours >= 12){ // 시간이 12보다 클 때 PM으로 세팅, 12를 빼줌
            amPm = 'PM';
            currentHours = addZeros(currentHours - 12,2);
        }

        if(currentSeconds >= 50){// 50초 이상일 때 색을 변환해 준다.
           currentSeconds = '<span style="color:#de1951;">'+currentSeconds+'</span>'
        }
        clock.innerHTML = currentHours+":"+currentMinute+":"+currentSeconds +" <span style='font-size:50px;'>"+ amPm+"</span>"; //날짜를 출력해 줌

        setTimeout("printClock()",1000);         // 1초마다 printClock() 함수 호출
}

    function addZeros(num, digit) { // 자릿수 맞춰주기
          var zero = '';
          num = num.toString();
          if (num.length < digit) {
            for (i = 0; i < digit - num.length; i++) {
              zero += '0';
            }
          }
          return zero + num;
    }


