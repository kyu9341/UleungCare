package com.example.uleungcare;

import android.content.DialogInterface;
import android.content.Intent;
import android.net.Uri;
import android.os.AsyncTask;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;
import org.w3c.dom.Text;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;

public class MainActivity extends AppCompatActivity {

    ImageButton cctvButton; // cctv화면으로 이동
    ImageButton controllerButton; // 리모컨 화면으로 이동
    ImageButton newButton; // 새로고침
    ImageButton settingButton; // 세팅화면으로 이동
    ImageButton powerButton; // 라즈베리파이 전원 종료
    float temperature; // 온도
    int powerOnOff = 0; // 라즈베리파이 전원
    String registered_dttm; // 측정시간
    TextView temText; // 현재 집 내부온도 출력
    String cctvURL; // 서버로부터 cctv를 확인할 수 있는 url을 응답받아 저장할 변수
    String toastMessage; // 눌린 버튼에 따른 toast 메세지 출력
    private AlertDialog dialog; // 알림창



    @Override
    protected void onCreate(Bundle savedInstanceState) {


        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        powerOnOff = 0;
        cctvButton = (ImageButton)findViewById(R.id.cctvButton); // 각 버튼 및 텍스트뷰 가져옴
        controllerButton = (ImageButton)findViewById(R.id.controllerButton);
        newButton = (ImageButton)findViewById(R.id.newButton);
        settingButton = (ImageButton)findViewById(R.id.settingButton);
        temText = (TextView)findViewById(R.id.temText);
        powerButton = (ImageButton)findViewById(R.id.powerButton);

        new MainActivity.BackgroundTask().execute(); // 데이터베이스 값 읽어오기

        newButton.setOnClickListener(new View.OnClickListener() { // 새로고침
            @Override
            public void onClick(View v) {
                new MainActivity.BackgroundTask().execute(); // 데이터베이스 값 읽어오기
            }
        });


        cctvButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent intent = new Intent(getApplicationContext(), CCTVActivity.class);  // CCTV 액티비티로 넘어감
                intent.putExtra("cctvURL", cctvURL); // cctvURL 같이 넘겨줌
                startActivity(intent);
            }
        });

        controllerButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), ControllerActivity.class); // 리모컨 액티비티로 이동
                startActivity(intent);
            }
        });

        settingButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), SettingActivity.class); // 세팅화면으로 이동
                startActivity(intent);
            }
        });

        powerButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                toastMessage = "우렝케어 종료";
                sendRequest();

            }
        });

        if(AppHelper.requestQueue == null){
            //리퀘스트큐 생성 (MainActivit가 메모리에서 만들어질 때 같이 생성이 될것이다.
            AppHelper.requestQueue = Volley.newRequestQueue(getApplicationContext());
        }

    }

    public void sendRequest(){ // 데이터를 서버에 전송하는 함수 - 각 버튼에 대한 정보를 한 번에 전송
        String url = "http://kyu9341.pythonanywhere.com/uleung/raspOnOff/";

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

                        AlertDialog.Builder builder = new AlertDialog.Builder(MainActivity.this);
                        dialog = builder.setMessage("우렁케어가 종료되었습니다.")
                                .setPositiveButton("확인", new DialogInterface.OnClickListener() {
                                    @Override
                                    public void onClick(DialogInterface dialog, int which) {
                                        ActivityCompat.finishAffinity(MainActivity.this);
                                        System.runFinalization();
                                        System.exit(0);
                                        //finish();
                                    }
                                })
                                .create();
                        dialog.show();
                        Toast.makeText(getApplicationContext(), toastMessage, Toast.LENGTH_SHORT).show(); // 서버에 전송이 성공한 경우 해당 토스트메시지 출력
                    } else {
                        Toast.makeText(getApplicationContext(), "전송 실패", Toast.LENGTH_SHORT).show();
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
                powerOnOff = 1;
                params.put("powerOnOff", powerOnOff+""); // tvOnOff 정보를 "tvOnOff"라는 키 값에 담아 서버로 전송
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

    class BackgroundTask extends AsyncTask<Void, Void, String>
    {
        String target;

        @Override
        protected void onPreExecute(){
            target = "http://kyu9341.pythonanywhere.com/uleung/getHomeInfo/"; // 라즈베리파이에서 측정한 HomeData를 받아올 url

        }

        @Override
        protected String doInBackground(Void... voids) {
            try{
                URL url = new URL(target);
                HttpURLConnection httpURLConnection = (HttpURLConnection)url.openConnection();
                InputStream inputStream = httpURLConnection.getInputStream(); // 넘어오는 결과값들을 저장
                BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream)); // 해당 inputstream에 있는 내용들을 버퍼에 담아 읽을수 있도록 함.
                String temp;
                StringBuilder stringBuilder = new StringBuilder(); // 문자열 형태로 저장
                while ((temp = bufferedReader.readLine()) != null){  // 버퍼에서 받아오는 값을 한줄씩 읽으면 temp에 저장
                    stringBuilder.append(temp + "\n");
                }
                bufferedReader.close();
                inputStream.close();
                httpURLConnection.disconnect();
                return stringBuilder.toString().trim();

            }catch (Exception e){
                e.printStackTrace();
            }

            return null;
        }

        @Override
        public void onProgressUpdate(Void... values){
            super.onProgressUpdate();
        }

        @Override
        public void onPostExecute(String result){ // 해당 결과 처리
            try{
                JSONObject jsonResponse = new JSONObject(result);

                temperature = jsonResponse.getInt("temperature"); // 서버로부터 집 내부온도 받아와 저장
                cctvURL = jsonResponse.getString("cctvURL"); // 서버로부터 cctvURL을 받아옴
                registered_dttm = jsonResponse.getString("registered_dttm"); // 데이터 저장 시간


                temText.setText("실내 온도 : "+ temperature); // 받아온 내부온도 출력

            }catch (Exception e){
                e.printStackTrace();
            }
        }


    }

}
