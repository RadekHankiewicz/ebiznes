package com.example

import io.ktor.client.*
import io.ktor.client.engine.apache.*
import io.ktor.client.request.*
import io.ktor.http.*
import io.ktor.client.plugins.contentnegotiation.*
import io.ktor.serialization.kotlinx.json.*
import kotlinx.serialization.json.Json
import io.ktor.client.plugins.logging.*
import kotlinx.serialization.Serializable


@Serializable
data class DiscordWebhookRequest(val content: String)

suspend fun main() {
    val webhook = "https://discord.com/api/webhooks/1096174254380302408/_EuBOoD83L_4DR1WUJNPY1EdBLzLfy63dEsUwwDCgGHretzzSmPnVAL1R-RWQAn37lRo"

    val client = HttpClient(Apache) {
        install(ContentNegotiation) {
            json(Json {
                prettyPrint = true
                isLenient = true })
        }
        install(Logging)
    }
    val message = DiscordWebhookRequest("Wiadomość")
    client.post(webhook) {
        contentType(ContentType.Application.Json)
        setBody(message)
    }
    client.close()
}