  function realTimer() {

		const nowDate = new Date();

		const year = nowDate.getFullYear();

		const month= nowDate.getMonth() + 1;

		const date = nowDate.getDate();

		const hour = nowDate.getHours();

		const min = nowDate.getMinutes();

		const sec = nowDate.getSeconds();

		document.getElementById("nowTimes").innerHTML =
                hour + ":" + addzero(min) + ":" + addzero(sec);
  };


        // 1자리수의 숫자인 경우 앞에 0을 붙여준다.

	function addzero(num) {

		if(num < 10) { num = "0" + num; }

 		return num;

	};

	function countdown(){
	    var now = new Date();
	    var year = now.getFullYear();
	    var month = now.getMonth()+1;
	    var day = now.getDate();

	    var hour = event_hour
	    var min = event_minute
	    var eventDate = new Date(year, month, day, hour, min);
	    console.log(eventDate)

		var currentTime = now.getTime();
		var eventTime = eventDate.getTime();


		var remTime = eventTime - currentTime;
		var s = Math.floor(remTime/1000);
		var m = Math.floor(s/60);
		var h = Math.floor(m/60);

		h %= 24;
		m %= 60;
		s %= 60;

		if (s == 15){
		    alarm();
		};
		if(s == 0){
		    alarm_back();
		};

		h = (h < 10) ? "0" + h : h;
        m = (m < 10) ? "0" + m : m;
        s = (s < 10) ? "0" + s : s;


        document.getElementById("hours").innerText = h;
	    document.getElementById("minutes").innerText = m;
	    document.getElementById("seconds").innerText = s;
	    setTimeout(countdown, 1000);
	};

	function alarm(){
	    var target = document.getElementById("alarm")
	    target.style.backgroundColor = "#A52A2A";
	};

	function alarm_back(){
	    var target = document.getElementById("alarm")
	    target.style.backgroundColor = "#FFFAF0";
	};

     function bring_data(realtimeStationArrival){
        alert("hello");

        var result = realtimeStationArrival

        var up = [];
        var down = [];
        var outbound = [];
        var inbound = [];
        var count = 0;

        if( result == 0 ){
             var target = document.getElementById("station");
             target.innerHTML = "<strong class = 'subway_info' >" + "열차 없습니다" +"</strong>";
        };

        for(i=0; i < result.length; i++){

            if(result[i]['updnLine'] == '상행' || result[i]['updnLine'] == '내선'){

                var target = document.getElementById("up");
                var new_span = document.createElement('li');
                new_span.innerHTML = "<strong class = 'subway_info' >" + result[i]['arvlMsg2'] +"</strong>";
                target.appendChild(new_span);

                var target2 = document.getElementById("up2");
                var new_span2 = document.createElement('li');
                new_span2.innerHTML = "<strong class = 'subway_info' >" + result[i]['arvlMsg3'] +"</strong>";
                target2.appendChild(new_span2);

            };
            if(result[i]['updnLine'] == '하행' || result[i]['updnLine'] == '외선'){
                var target = document.getElementById("down");
                var new_span = document.createElement('li');
                new_span.innerHTML = "<strong class = 'subway_info' >" + result[i]['arvlMsg2'] +"</strong>";
                target.appendChild(new_span);

                var target2 = document.getElementById("down2");
                var new_span2 = document.createElement('li');
                new_span2.innerHTML = "<strong class = 'subway_info' >" + result[i]['arvlMsg3'] +"</strong>";
                target2.appendChild(new_span2);
            };
        };
     };

  function fcstTrainFontColor() {
    var target = document.getElementsByClassName("subway_info")
    target.style.color="Red";
  }

// 설정된 시간의 += 15분 내의 지하철 시간표
  function timetable(up, down){
        var left_time = [];

        var now = new Date();
		var s = now.getSeconds();
		var m = now.getMinutes();
		var h = now.getHours();

		console.log(s, m, h)
    //  상행선 시간표
    for(i=0; i < up.length; i ++){

        var target = document.getElementById("upp");
        var new_span = document.createElement('li');

        var time = up[i][0].split(':')
        var arriveTime = time[0] + " 시 " + time[1] + " 분"
        var heading = " (" + up[i][2] + " 행)"

        new_span.innerHTML = "<strong class = 'subway_info' >" + arriveTime + heading +"</strong>";
        target.appendChild(new_span);

        // H : M : S
        var target_time = up[i][0].split(':')
        console.log(target_time)
        console.log(target_time[0]-h)
    };
    //  하행선 시간표
    for(i=0; i < down.length; i ++){
        var target = document.getElementById("downn");
        var new_span = document.createElement('li');

        var time = down[i][0].split(':')
        var arriveTime = time[0] + " 시 " + time[1] + " 분"
        var heading = " (" + down[i][2] + " 행)"

        new_span.innerHTML = "<strong class = 'subway_info' >" + arriveTime + heading +"</strong>";
        target.appendChild(new_span);

        //  H : M : S
        var target_time = down[i][0].split(':')
        console.log(target_time)
        console.log(target_time[0]-h)
    };
  };


   function recommendClothing(pop, now_temp, findDust){

            if(findDust[0] > 60 && findDust[1] > 70){
                var target = document.getElementById("mask")
                target.innerText = "KF90 마스크 챙기세요"
            }
            if(findDust[0] < 50 && findDust[1] < 50){
                var target = document.getElementById("mask")
                target.innerText = "필요없어요"
            }

            if (pop > 50){
                var target = document.getElementById("umbrella")
                target.innerText = '우산 챙겨요!'
            }
            else if(pop < 50){
                alert("fuc")
                var target = document.getElementById("umbrella")
                target.innerText = '필요없음!'
            };

            if ( now_temp < 5){
                  var target = document.getElementById("clothing")
                  target.innerHTML = "현재 너무 추워요.<br> 패딩, 두꺼운코트,<br> 목도리, 기모가 좋겠네요"
            }
            else if ( 5 <= now_temp && now_temp < 9){
                  var target = document.getElementById("clothing")
                  target.innerHTML = "현재 추워요.<br>  코트,경량패딩, 히트텍,<br> 니트, 레깅스가 좋겠네요"

            }
            else if ( 9 <= now_temp && now_temp < 17){
                  var target = document.getElementById("clothing")
                  target.innerHTML = "현재 쌀쌀해요.<br> 자켓, 트렌치코트,<br>야상, 니트, 청바지가 좋겠네요"

            }
            else if ( 17 <= now_temp && now_temp < 20){
                  var target = document.getElementById("clothing")
                  target.innerHTML = "현재 서늘해요.<br> 맨투맨, 얇은 니트, 가디건,<br> 청바지가 좋겠네요"
            }
            else if ( 20<= now_temp && now_temp < 23){
                  var target = document.getElementById("clothing")
                  target.innerHTML = "현재 선선해요.<br> 긴팔티, 얇은 가디건,<br> 면바지, 청바지가 좋겠네요"
            }
            else if (23 <= now_temp && now_temp < 26){
                  var target = document.getElementById("clothing")
                  target.innerHTML =  "<td class = 'outfit' >" + "반팔, 얇은 셔츠,<br> 반바지, 면바지가<br> 좋겠네요" +"</td>";
            }
            else if ( 26 <= now_temp && now_temp < 40 ){
                  var target = document.getElementById("clothing")
                  target.innerHTML ="현재 기온 더워요<br> 민소매, 반바지,<br> 원피스가 좋겠네요"
            };

        };