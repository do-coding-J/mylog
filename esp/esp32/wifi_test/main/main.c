#include <stdio.h>

#include "esp_wifi.h"
#include "esp_event.h"
#include "esp_log.h"
#include "freertos/FreeRTOS.h"
#include "freertos/event_groups.h"
#include "nvs_flash.h"

#define TAG "WIFI_SCAN"

static EventGroupHandle_t wifi_event_group;
const int WIFI_CONNECTEC_BIT = BIT0;

static void wifi_scan_done(void *arg, esp_event_base_t event_base, int32_t event_id, void *event_data)
{
    if (event_id == WIFI_EVENT_SCAN_DONE)
    {
        printf("wifi 스캔 완료\n");
        uint16_t ap_num = 0;
        esp_wifi_scan_get_ap_num(&ap_num);

        if (ap_num == 0)
        {
            printf("주변에 스캔 된 wifi가 없습니다.\n");
            return;
        }

        wifi_ap_record_t *ap_list = (wifi_ap_record_t *)malloc(sizeof(wifi_ap_record_t) * ap_num);
        if (!ap_list)
        {
            printf("메모리 할당 실패\n");
            return;
        }

        esp_wifi_scan_get_ap_records(&ap_num, ap_list);

        printf("스캔 된 wifi 목록\n");
        for (int i = 0; i < ap_num; i++)
        {
            printf("SSID : %s, RSSI : %d\n", (char *)ap_list[i].ssid, ap_list[i].rssi);
        }

        free(ap_list);
    }
}

void wifi_init_sta()
{
    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    ESP_ERROR_CHECK(esp_wifi_init(&cfg));
    ESP_ERROR_CHECK(esp_wifi_set_storage((WIFI_STORAGE_RAM)));

    // ESP_ERROR_CHECK(esp_event_handler_register(WIFI_EVENT, ESP_EVENT_ANY_ID, &wifi_scan_done, NULL));
    esp_event_handler_register(WIFI_EVENT, ESP_EVENT_ANY_ID, &wifi_scan_done, NULL);
    ESP_ERROR_CHECK(esp_wifi_set_mode(WIFI_MODE_STA));

    wifi_config_t wifi_config = {
        .sta = {
            .ssid = "curinginnos5G",
            .password = "05200520"}};

    ESP_ERROR_CHECK(esp_wifi_set_config(ESP_IF_WIFI_STA, &wifi_config));

    ESP_ERROR_CHECK(esp_wifi_start());
    ESP_LOGI(TAG, "wifi 연결 시작....");
}

void app_main(void)
{
    ESP_ERROR_CHECK(nvs_flash_init());
    wifi_init_sta();

    ESP_ERROR_CHECK(esp_wifi_scan_start(NULL, true));
}