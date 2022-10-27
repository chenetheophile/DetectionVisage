package com.example.authentification;
import android.content.Intent;
import android.net.Uri;
import android.net.http.SslError;
import android.view.View;
import android.webkit.SslErrorHandler;
import android.webkit.WebView;
import android.webkit.WebViewClient;
public class MyAppWebViewClient extends WebViewClient {

    @Override
    /*
     * La fonction shouldOverrideUrlLoading permet de restreindre l'url configurée avec loadurl
     * à une chaîne de caractère précise, soit le nom de domaine dans le script suivant
     */
    public boolean shouldOverrideUrlLoading(WebView view, String url) {
        return false;
    }
    @Override
    public void onReceivedSslError(WebView view, SslErrorHandler handler, SslError error) {
        handler.proceed(); // Ignore SSL certificate errors
    }
}