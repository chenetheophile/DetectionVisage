package com.example.authentification;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;

public class MainActivity extends AppCompatActivity {

    private WebView mWebView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mWebView = findViewById(R.id.activity_main_webview);
        WebSettings webSettings = mWebView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webSettings.setJavaScriptCanOpenWindowsAutomatically(true);
        webSettings.setDomStorageEnabled(true);
        mWebView.loadUrl("http://10.0.2.2:4200");
        mWebView.setWebViewClient(new MyAppWebViewClient() {
            @Override
            public void onPageFinished(WebView view, String url) {
//                 Cache le splashscreen imageLoading1 grâce à l'événement onPageFinished
                findViewById(R.id.imageLoading1).setVisibility(View.GONE);
                findViewById(R.id.progressBar).setVisibility(View.GONE);
//                 Permet d'afficher la page web à l'aide de la méthode webview
                findViewById(R.id.activity_main_webview).setVisibility(View.VISIBLE);
            }
        });

    }
}