package com.example.uleungcare;

import android.os.AsyncTask;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.HashMap;
import java.util.Map;

import static java.sql.DriverManager.println;

public class ControllerActivity extends AppCompatActivity {

    private int tvOnOff = 0; // TV 상태 ( 켜짐 : 1, 꺼짐 : 0)
    private int airconOnOff = 0; //  에어컨 상태 ( 켜짐 : 1, 꺼짐 : 0)
    private int airconTempUpDown = 0; // 에어컨 온도 up down
    private int tvChUpDown = 0; // TV 채널 up down
    private int tvVolUpDown = 0; //TV 볼륨 up down


    ImageButton tvonButton; // tvOnOff 버튼
    ImageButton airconOnButton; // 에어컨 OnOff 버튼
    ImageButton airUpButton; // 에어컨 온도 up 버튼
    ImageButton airDownButton; // 에어컨 온도 down 버튼
    ImageButton tvVolUpButton; // tv 음량 up 버튼
    ImageButton tvVolDownButton; // tv 음량 down 버튼
    ImageButton tvChUpButton;  // tv 채널 up 버튼
    ImageButton tvChDownButton;  // tv 채널 down 버튼튼

    private AlertDialog dialog; // 알림창
    String toastMessage; // 눌린 버튼에 따른 toast 메세지 출력

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_controller);

        tvonButton = (ImageButton)findViewById(R.id.tvonButton); // 각 버튼을 읽어옴
        airconOnButton = (ImageButton)findViewById(R.id.airconOnButton);
        airUpButton = (ImageButton)findViewById(R.id.airUpButton);
        airDownButton = (ImageButton)findViewById(R.id.airDownButton);
        tvChUpButton = (ImageButton)findViewById(R.id.tvChUpButton);
        tvChDownButton = (ImageButton)findViewById(R.id.tvChDownButton);
        tvVolUpButton = (ImageButton)findViewById(R.id.tvVolUpButton);
        tvVolDownButton = (ImageButton)findViewById(R.id.tvVolDownButton);



        tvonButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                if(tvOnOff == 0){ // 꺼짐 상태인 0 인경우
                    tvOnOff = 1;
                    toastMessage = "TV ON";
                }else{ // tv가 켜진경우
                    tvOnOff = 0;
                    toastMessage = "TV OFF";
                }
                sendRequest(); // 서버에 전송
            }
        });

        airconOnButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(airconOnOff == 0){ // 꺼짐 상태인 0 인경우
                    airconOnOff = 1;
                    toastMessage = "에어컨 ON";
                }else{ // 에어컨이 켜진경우
                    airconOnOff = 0;
                    toastMessage = "에어컨 OFF";
                }
                sendRequest();
            }
        });


        airUpButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                airconTempUpDown++; // 에어컨 온도 1 up
                sendRequest();
                toastMessage = "에어컨 온도 UP";

            }
        });

        airDownButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                airconTempUpDown--; // 에어컨 온도 1 down
                sendRequest();
                toastMessage = "에어컨 온도 DOWN";
            }
        });

        tvChUpButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tvChUpDown ++; // TV 채널 1 up
                toastMessage = "TV 채널 UP";
                sendRequest();

            }
        });

        tvChDownButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tvChUpDown --; // TV 채널 1 down
                toastMessage = "TV 채널 DOWN";
                sendRequest();
            }
        });

        tvVolUpButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tvVolUpDown++; // TV 음량 1 up
                toastMessage = "TV 음량 UP";
                sendRequest();
            }
        });

        tvVolDownButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tvVolUpDown = -1; // TV 음량 1 down
                toastMessage = "TV 음량 DOWN";
                sendRequest();
            }
        });



        if(AppHelper.requestQueue == null){
            //리퀘스트큐 생성 (MainActivit가 메모리에서 만들어질 때 같이 생성이 될것이다.
            AppHelper.requestQueue = Volley.newRequestQueue(getApplicationContext());
        }

    }

    public void sendRequest(){ // 데이터를 서버에 전송하는 함수 - 각 버튼에 대한 정보를 한 번에 전송
        String url = "http://kyu9341.pythonanywhere.com/uleung/AndroidControl/";

        //StringRequest를 만듬 (파라미터구분을 쉽게하기위해 엔터를 쳐서 구분하면 좋다)
        //StringRequest는 요청객체중 하나이며 가장 많이 쓰인다고한다.
        //요청객체는 다음고 같이 보내는방식(GET,POST), URL, 응답성공리스너, 응답실패리스너 이렇게 4개의 파라미터를 전달할 수 있다.(리퀘스트큐에 )
        //화면에 결과를 표시할때 핸들러를 사용하지 않아도되는 장점이있다.
        StringRequest request = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {  //응답을 문자열로 받아서 여기다 넣어달란말임(응답을 성공적으로 받았을 떄 이메소드가 자동으로 호출됨
                    @Override
                    public void onResponse(String response) {
                        Log.e("응답 => "+ response, "응답 => ");

                        try {
                            JSONObject jsonResponse = new JSONObject(response);
                            boolean success = jsonResponse.getBoolean("success");
                            if (success) {// 서버로부터의 json응답이 success인 경우(전송이 정상적으로 이루어진 경우)

                                Toast.makeText(getApplicationContext(), toastMessage, Toast.LENGTH_SHORT).show(); // 서버에 전송이 성공한 경우 해당 토스트메시지 출력
                            } else {
                                Toast.makeText(getApplicationContext(), "전송 실패", Toast.LENGTH_SHORT).show();
                            }
                            String kind = jsonResponse.getString("kind");

                            if(kind != ""){ // 서버의 응답에 따른 각 변수 초기화
                                if(kind.equals("temperature-")){
                                    airconTempUpDown--; // 서버에 전송 후 초기화
                                }else if(kind.equals("temperature+")){
                                    airconTempUpDown++;
                                }

                                if(kind.equals("channel-")){
                                    tvChUpDown --;
                                }else if(kind.equals("channel+")){
                                    tvChUpDown ++;
                                }

                                if(kind.equals("volume-")){
                                    tvVolUpDown --;
                                }else if(kind.equals("volume+")){
                                    tvVolUpDown++;
                                }
                            }

                        } catch (Exception e) {
                            e.printStackTrace();
                        }

                    }
                },
                new Response.ErrorListener(){ //에러발생시 호출될 리스너 객체
                    @Override
                    public void onErrorResponse(VolleyError error) {

                        Log.e("에러 => "+ error.getMessage(), "에러 => ");
                    }
                }
        ){
            //만약 POST 방식에서 전달할 요청 파라미터가 있다면 getParams 메소드에서 반환하는 HashMap 객체에 넣어줍니다.
            //이렇게 만든 요청 객체는 요청 큐에 넣어주는 것만 해주면 됩니다.
            //POST방식으로 안할거면 없어도 되는거같다.
            @Override
            protected Map<String, String> getParams() throws AuthFailureError {
                Map<String, String> params = new HashMap<String, String>();

                params.put("tvOnOff", tvOnOff+""); // tvOnOff 정보를 "tvOnOff"라는 키 값에 담아 서버로 전송
                params.put("airconOnOff", airconOnOff+"");
                params.put("airconTempUpDown", airconTempUpDown+"");
                params.put("tvChUpDown", tvChUpDown+"");
                params.put("tvVolUpDown", tvVolUpDown+"");

                return params;
            }

        };

        //아래 add코드처럼 넣어줄때 Volley라고하는게 내부에서 캐싱을 해준다, 즉, 한번 보내고 받은 응답결과가 있으면
        //그 다음에 보냈을 떄 이전 게 있으면 그냥 이전거를 보여줄수도  있다.
        //따라서 이렇게 하지말고 매번 받은 결과를 그대로 보여주기 위해 다음과같이 setShouldCache를 false로한다.
        //결과적으로 이전 결과가 있어도 새로 요청한 응답을 보여줌
        request.setShouldCache(false);
        AppHelper.requestQueue.add(request);


    }

}
