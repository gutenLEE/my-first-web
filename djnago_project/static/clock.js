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

     function bring_data(result){
        alert("hello");
        var up = [];
        var down = [];
        var outbound = [];
        var inbound = [];
        var count = 0;
        console.log(result)

        for(i=0; i < result.length; i++){

            if (result[i]['subwayId'] == line_code){
                alert(result[i]['subwayId'])
                if(result[i]['updnLine'] == '상행' || result[i]['updnLine'] == '내선'){

                    var target = document.getElementById("up");
                    var new_span = document.createElement('span');
                    new_span.innerHTML = "<strong class = 'subway_info' >" + result[i]['arvlMsg2'] +"</strong>";
                    target.appendChild(new_span);

                    var target2 = document.getElementById("up2");
                    var new_span2 = document.createElement('span');
                    new_span2.innerHTML = "<strong class = 'subway_info' >" + result[i]['arvlMsg3'] +"</strong>";
                    target2.appendChild(new_span2);

                };
                if(result[i]['updnLine'] == '하행' || result[i]['updnLine'] == '외선'){
                    var target = document.getElementById("down");
                    var new_span = document.createElement('span');
                    new_span.innerHTML = "<strong class = 'subway_info' >" + result[i]['arvlMsg2'] +"</strong>";
                    target.appendChild(new_span);

                    var target2 = document.getElementById("down2");
                    var new_span2 = document.createElement('span');
                    new_span2.innerHTML = "<strong class = 'subway_info' >" + result[i]['arvlMsg3'] +"</strong>";
                    target2.appendChild(new_span2);

                };
            };
        };
     };

  function timetable(up, down){
        var left_time = [];
        var now = new Date();
		var s = now.getSeconds();
		var m = now.getMinutes();
		var h = now.getHours();

		console.log(s, m, h)

    for(i=0; i < up.length; i ++){
        var target = document.getElementById("upp");
        var new_span = document.createElement('li');
        new_span.innerHTML = "<strong class = 'subway_info' >" + up[i][0] +"</strong>";
        target.appendChild(new_span);

        var test = up[i][0].split(':')
        console.log(test)
        console.log(test[0]-h)
    };

  };