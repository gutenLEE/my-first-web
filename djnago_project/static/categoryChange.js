     function categoryChange(elementId) {
                console.log(test)
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