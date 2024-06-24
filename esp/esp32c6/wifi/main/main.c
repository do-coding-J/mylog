#include <stdio.h>
#include "esp_log.h"
#include "esp_wifi.h"
#include "esp_event.h"
#include "freertos/task.h"
#include "freertos/FreeRTOS.h"
#include "nvs_flash.h"

#define SCAN_TAG "WIFI_SCAN"
#define CON_TAG "WIFI_CONN"

void wifi_initialize();
void wifi_scan_task(void *pvParameters);
void wifi_deinitialize();

void wifi_event_handler(void *arg, esp_event_base_t event_base, int32_t event_id, void *event_data);

void app_main(void)
{
    ESP_ERROR_CHECK(nvs_flash_init());

    xTaskCreate(wifi_scan_task, "wifi scan task", 4096, NULL, 0, NULL);
}

void wifi_initialize()
{

    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    ESP_ERROR_CHECK(esp_wifi_init(&cfg));

    ESP_ERROR_CHECK(esp_event_loop_create_default());

    esp_event_handler_instance_t instance_any_id;
    esp_event_handler_instance_register(WIFI_EVENT, ESP_EVENT_ANY_ID, wifi_event_handler, NULL, &instance_any_id);

    wifi_config_t wifi_cfg = {
        .ap = {
            .ssid = "ESP32C6",
            .ssid_len = 0,
            .channel = 0,
            .password = "NULLNULL",
            .max_connection = 4,
            .authmode = WIFI_AUTH_WPA_WPA2_PSK},
    };

    wifi_mode_t wifi_mode = WIFI_MODE_APSTA;
    ESP_ERROR_CHECK(esp_wifi_set_mode(wifi_mode));
    wifi_interface_t wifi_interface = ESP_IF_WIFI_STA;
    ESP_ERROR_CHECK(esp_wifi_set_config(wifi_interface, &wifi_cfg));

    ESP_ERROR_CHECK(esp_wifi_start());
}

void wifi_scan_task(void *pvParameters)
{
    wifi_initialize();

    while (1)
    {

        ESP_LOGI(SCAN_TAG, "Start Scanning");
        wifi_scan_config_t scan_cfg =
            {
                .ssid = NULL,
                .bssid = NULL,
                .channel = 0,
                .show_hidden = true};
        ESP_ERROR_CHECK(esp_wifi_scan_start(&scan_cfg, true));

        uint16_t ap_num;
        esp_wifi_scan_get_ap_num(&ap_num);
        ESP_LOGI(SCAN_TAG, "Scanned AP %d", ap_num);

        wifi_ap_record_t *ap_records = (wifi_ap_record_t *)malloc(sizeof(wifi_ap_record_t) * ap_num);
        ESP_ERROR_CHECK(esp_wifi_scan_get_ap_records(&ap_num, ap_records));

        for (int i = 0; i < ap_num; i++)
        {
            ESP_LOGI(SCAN_TAG, "SSID: %s, RSSI: %d", ap_records[i].ssid, ap_records[i].rssi);
        }

        free(ap_records);
        vTaskDelay(pdMS_TO_TICKS(20000)); // 20초 대기
    }

    wifi_deinitialize();
}

void wifi_deinitialize()
{
    esp_wifi_stop();
    esp_wifi_deinit();
}

void wifi_event_handler(void *arg, esp_event_base_t event_base, int32_t event_id, void *event_data)
{
    ESP_LOGI(CON_TAG, "connection attempt");
}