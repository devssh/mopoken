def index():
    return """
    <!DOCTYPE html>
       <html> 
       <head>
       <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
       </head>
       <body>
        <h2 style="">Enter inputs</h2>
        <div style="display: flex; flex-direction: column; width: 70vw; height:40vh; border: 1px solid black;">
            
            <div style="display: flex; flex-direction: row;">
            <div style="width: 17vw;margin-left: 1em; margin-top: 1em;">Enter player mopoken</div>
            <input type="text" id="input1" style="width: 30vw;height: 2vh; margin-left: 2em; margin-top: 2em; margin-bottom: 3em;" 
            value="Fire#10;Water#20;Fighting#6;Psychic#10;Electric#12"/>
            </div>
            
            <div style="display: flex; flex-direction: row;">
            <div style="width: 17vw;margin-left: 1em;">Enter npc mopoken</div>
            <input type="text" id="input2" style="width: 30vw;height: 2vh; margin-left: 2em; margin-bottom: 3em;" 
            value="Water#10;Fighting#10;Psychic#10;Fire#12;Grass#2"/>
            </div>
            
            <input type="submit" id="submit" style="width: 20vw; height: 5vh; margin-left: 2em; margin-bottom: 2em;
            border: 0px;background-color: #333;border-radius: 3px;color: #fff;text-align: center;" value="Submit"/>
        </div>
        <div id="result" style="border: 1px solid black; width: 40vw; height: 10vh; margin-top: 2em;font-size: 0.8em;
        padding-top: 1em;padding-left: 1em;"></div>
        <script>
        $(document).ready(function(){
          $("#submit").click(function(){
            $.ajax({
            type: "post",
            url: "run",
            data: {input1: $('#input1').val(), input2: $('#input2').val() },
            contentType: "application/x-www-form-urlencoded",
            success: function(responseData, textStatus, jqXHR) {
                $("#result").html(responseData);
            }
            });
          });
        });
        </script>
       </body>
       </html>
           """
