# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.


class Lobby(object):

    def __init__(self, params=None):
        if params is None:
            self.__lobby_id = None
            self.__owner_id = None
            self.__name = None
            self.__description = None
            self.__service_class = None
            self.__notification_type = None
            self.__notification_url = None
            self.__notification_game_name = None
            self.__logging = None
            self.__logging_date = None
            self.__create_room_trigger_script = None
            self.__create_room_done_trigger_script = None
            self.__delete_room_trigger_script = None
            self.__delete_room_done_trigger_script = None
            self.__create_subscribe_trigger_script = None
            self.__create_subscribe_done_trigger_script = None
            self.__delete_subscribe_trigger_script = None
            self.__delete_subscribe_done_trigger_script = None
            self.__send_message_trigger_script = None
            self.__send_message_done_trigger_script = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_lobby_id(params['lobbyId'] if 'lobbyId' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_notification_type(params['notificationType'] if 'notificationType' in params.keys() else None)
            self.set_notification_url(params['notificationUrl'] if 'notificationUrl' in params.keys() else None)
            self.set_notification_game_name(params['notificationGameName'] if 'notificationGameName' in params.keys() else None)
            self.set_logging(params['logging'] if 'logging' in params.keys() else None)
            self.set_logging_date(params['loggingDate'] if 'loggingDate' in params.keys() else None)
            self.set_create_room_trigger_script(params['createRoomTriggerScript'] if 'createRoomTriggerScript' in params.keys() else None)
            self.set_create_room_done_trigger_script(params['createRoomDoneTriggerScript'] if 'createRoomDoneTriggerScript' in params.keys() else None)
            self.set_delete_room_trigger_script(params['deleteRoomTriggerScript'] if 'deleteRoomTriggerScript' in params.keys() else None)
            self.set_delete_room_done_trigger_script(params['deleteRoomDoneTriggerScript'] if 'deleteRoomDoneTriggerScript' in params.keys() else None)
            self.set_create_subscribe_trigger_script(params['createSubscribeTriggerScript'] if 'createSubscribeTriggerScript' in params.keys() else None)
            self.set_create_subscribe_done_trigger_script(params['createSubscribeDoneTriggerScript'] if 'createSubscribeDoneTriggerScript' in params.keys() else None)
            self.set_delete_subscribe_trigger_script(params['deleteSubscribeTriggerScript'] if 'deleteSubscribeTriggerScript' in params.keys() else None)
            self.set_delete_subscribe_done_trigger_script(params['deleteSubscribeDoneTriggerScript'] if 'deleteSubscribeDoneTriggerScript' in params.keys() else None)
            self.set_send_message_trigger_script(params['sendMessageTriggerScript'] if 'sendMessageTriggerScript' in params.keys() else None)
            self.set_send_message_done_trigger_script(params['sendMessageDoneTriggerScript'] if 'sendMessageDoneTriggerScript' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

    def get_lobby_id(self):
        """
        ロビーGRNを取得
        :return: ロビーGRN
        :rtype: unicode
        """
        return self.__lobby_id

    def set_lobby_id(self, lobby_id):
        """
        ロビーGRNを設定
        :param lobby_id: ロビーGRN
        :type lobby_id: unicode
        """
        self.__lobby_id = lobby_id

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

    def get_name(self):
        """
        ゲーム名を取得
        :return: ゲーム名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        ゲーム名を設定
        :param name: ゲーム名
        :type name: unicode
        """
        self.__name = name

    def get_description(self):
        """
        説明文を取得
        :return: 説明文
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        """
        self.__description = description

    def get_service_class(self):
        """
        サービスクラスを取得
        :return: サービスクラス
        :rtype: unicode
        """
        return self.__service_class

    def set_service_class(self, service_class):
        """
        サービスクラスを設定
        :param service_class: サービスクラス
        :type service_class: unicode
        """
        self.__service_class = service_class

    def get_notification_type(self):
        """
        通知方式を取得
        :return: 通知方式
        :rtype: unicode
        """
        return self.__notification_type

    def set_notification_type(self, notification_type):
        """
        通知方式を設定
        :param notification_type: 通知方式
        :type notification_type: unicode
        """
        self.__notification_type = notification_type

    def get_notification_url(self):
        """
        http/https を選択した際の通知先URLを取得
        :return: http/https を選択した際の通知先URL
        :rtype: unicode
        """
        return self.__notification_url

    def set_notification_url(self, notification_url):
        """
        http/https を選択した際の通知先URLを設定
        :param notification_url: http/https を選択した際の通知先URL
        :type notification_url: unicode
        """
        self.__notification_url = notification_url

    def get_notification_game_name(self):
        """
        gs2-in-game-push-notification を選択した際の GS2-InGamePushNotification のゲーム名を取得
        :return: gs2-in-game-push-notification を選択した際の GS2-InGamePushNotification のゲーム名
        :rtype: unicode
        """
        return self.__notification_game_name

    def set_notification_game_name(self, notification_game_name):
        """
        gs2-in-game-push-notification を選択した際の GS2-InGamePushNotification のゲーム名を設定
        :param notification_game_name: gs2-in-game-push-notification を選択した際の GS2-InGamePushNotification のゲーム名
        :type notification_game_name: unicode
        """
        self.__notification_game_name = notification_game_name

    def get_logging(self):
        """
        ログを記録するかを取得
        :return: ログを記録するか
        :rtype: bool
        """
        return self.__logging

    def set_logging(self, logging):
        """
        ログを記録するかを設定
        :param logging: ログを記録するか
        :type logging: bool
        """
        self.__logging = logging

    def get_logging_date(self):
        """
        ログを記録する日数を取得
        :return: ログを記録する日数
        :rtype: int
        """
        return self.__logging_date

    def set_logging_date(self, logging_date):
        """
        ログを記録する日数を設定
        :param logging_date: ログを記録する日数
        :type logging_date: int
        """
        self.__logging_date = logging_date

    def get_create_room_trigger_script(self):
        """
        ルーム作成時 に実行されるGS2-Scriptを取得
        :return: ルーム作成時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__create_room_trigger_script

    def set_create_room_trigger_script(self, create_room_trigger_script):
        """
        ルーム作成時 に実行されるGS2-Scriptを設定
        :param create_room_trigger_script: ルーム作成時 に実行されるGS2-Script
        :type create_room_trigger_script: unicode
        """
        self.__create_room_trigger_script = create_room_trigger_script

    def get_create_room_done_trigger_script(self):
        """
        ルーム作成完了時 に実行されるGS2-Scriptを取得
        :return: ルーム作成完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__create_room_done_trigger_script

    def set_create_room_done_trigger_script(self, create_room_done_trigger_script):
        """
        ルーム作成完了時 に実行されるGS2-Scriptを設定
        :param create_room_done_trigger_script: ルーム作成完了時 に実行されるGS2-Script
        :type create_room_done_trigger_script: unicode
        """
        self.__create_room_done_trigger_script = create_room_done_trigger_script

    def get_delete_room_trigger_script(self):
        """
        ルーム削除時 に実行されるGS2-Scriptを取得
        :return: ルーム削除時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__delete_room_trigger_script

    def set_delete_room_trigger_script(self, delete_room_trigger_script):
        """
        ルーム削除時 に実行されるGS2-Scriptを設定
        :param delete_room_trigger_script: ルーム削除時 に実行されるGS2-Script
        :type delete_room_trigger_script: unicode
        """
        self.__delete_room_trigger_script = delete_room_trigger_script

    def get_delete_room_done_trigger_script(self):
        """
        ルーム削除完了時 に実行されるGS2-Scriptを取得
        :return: ルーム削除完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__delete_room_done_trigger_script

    def set_delete_room_done_trigger_script(self, delete_room_done_trigger_script):
        """
        ルーム削除完了時 に実行されるGS2-Scriptを設定
        :param delete_room_done_trigger_script: ルーム削除完了時 に実行されるGS2-Script
        :type delete_room_done_trigger_script: unicode
        """
        self.__delete_room_done_trigger_script = delete_room_done_trigger_script

    def get_create_subscribe_trigger_script(self):
        """
        ルーム購読時 に実行されるGS2-Scriptを取得
        :return: ルーム購読時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__create_subscribe_trigger_script

    def set_create_subscribe_trigger_script(self, create_subscribe_trigger_script):
        """
        ルーム購読時 に実行されるGS2-Scriptを設定
        :param create_subscribe_trigger_script: ルーム購読時 に実行されるGS2-Script
        :type create_subscribe_trigger_script: unicode
        """
        self.__create_subscribe_trigger_script = create_subscribe_trigger_script

    def get_create_subscribe_done_trigger_script(self):
        """
        ルーム購読完了時 に実行されるGS2-Scriptを取得
        :return: ルーム購読完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__create_subscribe_done_trigger_script

    def set_create_subscribe_done_trigger_script(self, create_subscribe_done_trigger_script):
        """
        ルーム購読完了時 に実行されるGS2-Scriptを設定
        :param create_subscribe_done_trigger_script: ルーム購読完了時 に実行されるGS2-Script
        :type create_subscribe_done_trigger_script: unicode
        """
        self.__create_subscribe_done_trigger_script = create_subscribe_done_trigger_script

    def get_delete_subscribe_trigger_script(self):
        """
        ルーム購読解除時 に実行されるGS2-Scriptを取得
        :return: ルーム購読解除時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__delete_subscribe_trigger_script

    def set_delete_subscribe_trigger_script(self, delete_subscribe_trigger_script):
        """
        ルーム購読解除時 に実行されるGS2-Scriptを設定
        :param delete_subscribe_trigger_script: ルーム購読解除時 に実行されるGS2-Script
        :type delete_subscribe_trigger_script: unicode
        """
        self.__delete_subscribe_trigger_script = delete_subscribe_trigger_script

    def get_delete_subscribe_done_trigger_script(self):
        """
        ルーム購読解除完了時 に実行されるGS2-Scriptを取得
        :return: ルーム購読解除完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__delete_subscribe_done_trigger_script

    def set_delete_subscribe_done_trigger_script(self, delete_subscribe_done_trigger_script):
        """
        ルーム購読解除完了時 に実行されるGS2-Scriptを設定
        :param delete_subscribe_done_trigger_script: ルーム購読解除完了時 に実行されるGS2-Script
        :type delete_subscribe_done_trigger_script: unicode
        """
        self.__delete_subscribe_done_trigger_script = delete_subscribe_done_trigger_script

    def get_send_message_trigger_script(self):
        """
        メッセージ送信時 に実行されるGS2-Scriptを取得
        :return: メッセージ送信時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__send_message_trigger_script

    def set_send_message_trigger_script(self, send_message_trigger_script):
        """
        メッセージ送信時 に実行されるGS2-Scriptを設定
        :param send_message_trigger_script: メッセージ送信時 に実行されるGS2-Script
        :type send_message_trigger_script: unicode
        """
        self.__send_message_trigger_script = send_message_trigger_script

    def get_send_message_done_trigger_script(self):
        """
        メッセージ送信完了時 に実行されるGS2-Scriptを取得
        :return: メッセージ送信完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__send_message_done_trigger_script

    def set_send_message_done_trigger_script(self, send_message_done_trigger_script):
        """
        メッセージ送信完了時 に実行されるGS2-Scriptを設定
        :param send_message_done_trigger_script: メッセージ送信完了時 に実行されるGS2-Script
        :type send_message_done_trigger_script: unicode
        """
        self.__send_message_done_trigger_script = send_message_done_trigger_script

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def to_dict(self):
        return {
            "lobbyId": self.__lobby_id,
            "ownerId": self.__owner_id,
            "name": self.__name,
            "description": self.__description,
            "serviceClass": self.__service_class,
            "notificationType": self.__notification_type,
            "notificationUrl": self.__notification_url,
            "notificationGameName": self.__notification_game_name,
            "logging": self.__logging,
            "loggingDate": self.__logging_date,
            "createRoomTriggerScript": self.__create_room_trigger_script,
            "createRoomDoneTriggerScript": self.__create_room_done_trigger_script,
            "deleteRoomTriggerScript": self.__delete_room_trigger_script,
            "deleteRoomDoneTriggerScript": self.__delete_room_done_trigger_script,
            "createSubscribeTriggerScript": self.__create_subscribe_trigger_script,
            "createSubscribeDoneTriggerScript": self.__create_subscribe_done_trigger_script,
            "deleteSubscribeTriggerScript": self.__delete_subscribe_trigger_script,
            "deleteSubscribeDoneTriggerScript": self.__delete_subscribe_done_trigger_script,
            "sendMessageTriggerScript": self.__send_message_trigger_script,
            "sendMessageDoneTriggerScript": self.__send_message_done_trigger_script,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
