package com.example.uleungcare;

import android.content.Intent;
import android.net.Uri;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONObject;
import org.w3c.dom.Text;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class MainActivity extends AppCompatActivity {

    ImageButton cctvButton;
    ImageButton controllerButton;
    ImageButton newButton;
    ImageButton settingButton;
    float temperature; // 온도
    int airconTem; // 현재 에어컨 설정 온도
    String registered_dttm; // 측정시간
    TextView temText;
    String cctvURL;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        cctvButton = (ImageButton)findViewById(R.id.cctvButton);
        controllerButton = (ImageButton)findViewById(R.id.controllerButton);
        newButton = (ImageButton)findViewById(R.id.newButton);
        settingButton = (ImageButton)findViewById(R.id.settingButton);
        temText = (TextView)findViewById(R.id.temText);

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

//                Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.naver.com/"));
                Intent intent = new Intent(getApplicationContext(), CCTVActivity.class);  // 메인 액티비티로 넘어감
                intent.putExtra("cctvURL", cctvURL);
                startActivity(intent);
            }
        });

        controllerButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), ControllerActivity.class);
                startActivity(intent);
            }
        });

        settingButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), SettingActivity.class);
                startActivity(intent);
            }
        });

    }



    class BackgroundTask extends AsyncTask<Void, Void, String>
    {
        String target;

        @Override
        protected void onPreExecute(){
            target = "http://kyu9341.pythonanywhere.com/uleung/getHomeInfo/";


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

                temperature = jsonResponse.getInt("temperature");
                airconTem = jsonResponse.getInt("airconTem");
                cctvURL = jsonResponse.getString("cctvURL");
                registered_dttm = jsonResponse.getString("registered_dttm");
/*
                JSONObject jsonObject = new JSONObject(result); // 응답 부분 처리
                JSONArray jsonArray = jsonObject.getJSONArray("home_data");

                JSONObject object = jsonArray.getJSONObject(0); // 현재 배열의 원소값

                temperature = object.getInt("temperature");
                humidity = object.getInt("humidity");
                registered_dttm = object.getString("registered_dttm");
*/

                Log.e("temperature = "+temperature, "temperature");
                Log.e("airconTem = "+airconTem, "airconTem");
                Log.e("cctvURL = "+cctvURL, "cctvURL");


                temText.setText("실내 온도 : "+ temperature);


            }catch (Exception e){
                e.printStackTrace();
            }
        }


    }

}
