package com.lanjed.sokogardenapp

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.ProgressBar
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.recyclerview.widget.RecyclerView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

//        signup intent
        val signup = findViewById<Button>(R.id.signup)
        signup.setOnClickListener {
            val intent = Intent(applicationContext, Signup::class.java)
            startActivity(intent)
        }

//        signin intent
        val signin = findViewById<Button>(R.id.signin)
        signin.setOnClickListener {
            val intent = Intent(applicationContext,Signin::class.java)
            startActivity(intent)
        }

        //        speech to text intent
        val speechToText = findViewById<Button>(R.id.speechToText)
        speechToText.setOnClickListener {
            val intent = Intent(applicationContext, SpeechToText::class.java)
            startActivity(intent)
        }

//        product fetch implementation
        val progressbar = findViewById<ProgressBar>(R.id.progressbar)
        val recyclerView = findViewById<RecyclerView>(R.id.recyclerView)

//        products source url
        val url = "http://jeddy.alwaysdata.net/api/get_product_details"

        val helper = ApiHelper(applicationContext)

        helper.loadProducts(url,recyclerView,progressbar)

    }
}