    function bring_data(){
        alert("hello");
        var up = [];
        var down = [];
        var outbound = [];
        var inbound = [];
        var count = 0;

        for(i=0; i < result.length; i++){

            if (result[i]['subwayId'] == line_code){
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

                    var target2 = document.getElementById("down");
                    var new_span2 = document.createElement('span');
                    new_span2.innerHTML = "<strong class = 'subway_info' >" + result[i]['arvlMsg3'] +"</strong>";
                    target2.appendChild(new_span2);

                };
            };
        };
    };



//       switch(true) {
//                      case result[i]['updnLine']=='상행':
//                           up.push(result[i]);
//                           console.log(up);
//                            break;
//                      case result[i]['updnLine']=='하행':
//                            down.push(result[i]);
//                            console.log(down);
//                            break;
//                      case result[i]['updnLine']=='외선':
//                            outbound.push(result[i]);
//                            console.log(outbound);
//                            break;
//                      default:  inbound.push(result[i]);
//                                console.log(inbound);
//                };

