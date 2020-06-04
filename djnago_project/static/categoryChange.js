     function categoryChange(elementId) {

                gu_list = [];
                var selected_city = document.getElementById("city_select").value
                var selected_gu = document.getElementById("gu_select").value;
                var target = document.getElementById(elementId);

                //구 리스트 추출
                for(var i=0; i < addr.length; i++) {
                    //선택된 1단계 구역의 행정동 리스트
                    var city_check = addr[i][0];
                    if( city_check.indexOf(selected_city) != -1){

                        // 1단계만 존재하는 구역
                        if( addr[i][1] == ""){
                        }
                        else{
                            if (gu_list.indexOf(addr[i][1]) == -1){
                                gu_list.push(addr[i][1]);
                            }
                        }
                    }
                };

                if( target.options.length > 1 ) {
                    var len = target.options.length;
                    for( var i = 1; i < len; i++ ) {
                        target.remove(1);
                    }
                }


                    // to create select options
                for (i = 0; i < gu_list.length; i++){
                    var opt = document.createElement('option');
                    opt.value = gu_list[i];
                    opt.innerHTML = gu_list[i];
                    target.appendChild(opt);
                }

            };

            function category_dong(elementId) {

                dong_list = [];

                var target = document.getElementById(elementId);
                var selected_gu = document.getElementById("gu_select").value;
                var selected_city = document.getElementById("city_select").value;

                // 동 리스트 추출
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

               var len = target.options.length
               for ( i = 0; i < len; i++){
                    target.options.remove(1)
               }

                // to create select options
                for (i = 0; i < dong_list.length; i++){
                        var opt = document.createElement('option');
                        opt.value = dong_list[i];
                        opt.innerHTML = dong_list[i];
                        target.appendChild(opt);
                };

            function inputCheck(){

            };  //input_check 함수 끝
        };

        function suggestion(){
            alert(now_temp)
            if ( now_temp < 5){
                  var target = document.getElementById("suggestion");
                  var insert = document.createElement("div");
                  insert.setAttribute('class','outfit_suggestion')
                  insert.innerHTML = "<p class = 'outfit' >" + "현재 기온 너무 추워요. 패딩, 두꺼운코트,<br> 목도리, 기모가 좋겠네요" +"</p>";
                  target.appendChild(insert);
            }
            else if ( 5 <= now_temp && now_temp < 9){
                  var target = document.getElementById("suggestion");
                  var insert = document.createElement("div");
                  insert.setAttribute('class','outfit_suggestion')
                  insert.innerHTML = "<p class = 'outfit' >" + "현재 기온 추워요.<br>  코트,경량패딩, 히트텍, 니트, 레깅스가 좋겠네요" +"</p>";
                  target.appendChild(insert);
            }
            else if ( 9 <= now_temp && now_temp < 17){
                  var target = document.getElementById("suggestion");
                  var insert = document.createElement("div");
                  insert.setAttribute('class','outfit_suggestion')
                  insert.innerHTML = "<p class = 'outfit' >" + "현재 기온 쌀쌀해요. 자켓, 트렌치코트,<br>야상, 니트, 청바지가 좋겠네요" +"</p>";
                  target.appendChild(insert);
            }
            else if ( 17 <= now_temp && now_temp < 20){
                  var target = document.getElementById("suggestion");
                  var insert = document.createElement("div");
                  insert.setAttribute('class','outfit_suggestion')
                  insert.innerHTML = "<p class = 'outfit' >" + "현재 기온 서늘해요. 맨투맨, 얇은 니트, 가디건, 청바지가 좋겠네요" +"</p>";
                  target.appendChild(insert);
            }
            else if ( 20<= now_temp && now_temp < 23){
                  var target = document.getElementById("suggestion");
                  var insert = document.createElement("div");
                  insert.setAttribute('class','outfit_suggestion')
                  insert.innerHTML = "<p class = 'outfit' >" + "현재 기온 선선해요. 긴팔티, 얇은 가디건, 면바지, 청바지가 좋겠네요" +"</p>";
                  target.appendChild(insert);
            }
            else if (23 <= now_temp && now_temp < 26){

                  var target = document.getElementById("suggestion");
                  var insert = document.createElement("div");
                  insert.setAttribute('class','outfit_suggestion')
                  insert.innerHTML = "<p class = 'outfit' >" + "현재 날씨에는 반팔, 얇은 셔츠, 반바지, 면바지가 좋겠네요" +"</p>";
                  target.appendChild(insert);
            }
            else if ( now_temp <= 26){
                  var target = document.getElementById("suggestion");
                  var insert = document.createElement("div");
                  insert.setAttribute('class','outfit_suggestion')
                  insert.innerHTML = "<p class = 'outfit' >" + "현재 기온 더워요 민소매, 반바지, 원피스가 좋겠네요" +"</p>";
                  target.appendChild(insert);
            };

       };