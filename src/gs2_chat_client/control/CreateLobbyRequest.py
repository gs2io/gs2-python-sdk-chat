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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_chat_client.Gs2Chat import Gs2Chat


class CreateLobbyRequest(Gs2BasicRequest):

    class Constant(Gs2Chat):
        FUNCTION = "CreateLobby"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateLobbyRequest, self).__init__(params)
        if params is None:
            self.__name = None
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)
        if params is None:
            self.__description = None
        else:
            self.set_description(params['description'] if 'description' in params.keys() else None)
        if params is None:
            self.__service_class = None
        else:
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
        if params is None:
            self.__notification_type = None
        else:
            self.set_notification_type(params['notificationType'] if 'notificationType' in params.keys() else None)
        if params is None:
            self.__notification_url = None
        else:
            self.set_notification_url(params['notificationUrl'] if 'notificationUrl' in params.keys() else None)
        if params is None:
            self.__notification_game_name = None
        else:
            self.set_notification_game_name(params['notificationGameName'] if 'notificationGameName' in params.keys() else None)
        if params is None:
            self.__logging = None
        else:
            self.set_logging(params['logging'] if 'logging' in params.keys() else None)
        if params is None:
            self.__logging_date = None
        else:
            self.set_logging_date(params['loggingDate'] if 'loggingDate' in params.keys() else None)
        if params is None:
            self.__create_room_trigger_script = None
        else:
            self.set_create_room_trigger_script(params['createRoomTriggerScript'] if 'createRoomTriggerScript' in params.keys() else None)
        if params is None:
            self.__create_room_done_trigger_script = None
        else:
            self.set_create_room_done_trigger_script(params['createRoomDoneTriggerScript'] if 'createRoomDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__delete_room_trigger_script = None
        else:
            self.set_delete_room_trigger_script(params['deleteRoomTriggerScript'] if 'deleteRoomTriggerScript' in params.keys() else None)
        if params is None:
            self.__delete_room_done_trigger_script = None
        else:
            self.set_delete_room_done_trigger_script(params['deleteRoomDoneTriggerScript'] if 'deleteRoomDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__create_subscribe_trigger_script = None
        else:
            self.set_create_subscribe_trigger_script(params['createSubscribeTriggerScript'] if 'createSubscribeTriggerScript' in params.keys() else None)
        if params is None:
            self.__create_subscribe_done_trigger_script = None
        else:
            self.set_create_subscribe_done_trigger_script(params['createSubscribeDoneTriggerScript'] if 'createSubscribeDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__delete_subscribe_trigger_script = None
        else:
            self.set_delete_subscribe_trigger_script(params['deleteSubscribeTriggerScript'] if 'deleteSubscribeTriggerScript' in params.keys() else None)
        if params is None:
            self.__delete_subscribe_done_trigger_script = None
        else:
            self.set_delete_subscribe_done_trigger_script(params['deleteSubscribeDoneTriggerScript'] if 'deleteSubscribeDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__send_message_trigger_script = None
        else:
            self.set_send_message_trigger_script(params['sendMessageTriggerScript'] if 'sendMessageTriggerScript' in params.keys() else None)
        if params is None:
            self.__send_message_done_trigger_script = None
        else:
            self.set_send_message_done_trigger_script(params['sendMessageDoneTriggerScript'] if 'sendMessageDoneTriggerScript' in params.keys() else None)

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
        if name and not isinstance(name, unicode):
            raise TypeError(type(name))
        self.__name = name

    def with_name(self, name):
        """
        ゲーム名を設定
        :param name: ゲーム名
        :type name: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_name(name)
        return self

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
        if description and not isinstance(description, unicode):
            raise TypeError(type(description))
        self.__description = description

    def with_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_description(description)
        return self

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
        if service_class and not isinstance(service_class, unicode):
            raise TypeError(type(service_class))
        self.__service_class = service_class

    def with_service_class(self, service_class):
        """
        サービスクラスを設定
        :param service_class: サービスクラス
        :type service_class: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_service_class(service_class)
        return self

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
        if notification_type and not isinstance(notification_type, unicode):
            raise TypeError(type(notification_type))
        self.__notification_type = notification_type

    def with_notification_type(self, notification_type):
        """
        通知方式を設定
        :param notification_type: 通知方式
        :type notification_type: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_notification_type(notification_type)
        return self

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
        if notification_url and not isinstance(notification_url, unicode):
            raise TypeError(type(notification_url))
        self.__notification_url = notification_url

    def with_notification_url(self, notification_url):
        """
        http/https を選択した際の通知先URLを設定
        :param notification_url: http/https を選択した際の通知先URL
        :type notification_url: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_notification_url(notification_url)
        return self

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
        if notification_game_name and not isinstance(notification_game_name, unicode):
            raise TypeError(type(notification_game_name))
        self.__notification_game_name = notification_game_name

    def with_notification_game_name(self, notification_game_name):
        """
        gs2-in-game-push-notification を選択した際の GS2-InGamePushNotification のゲーム名を設定
        :param notification_game_name: gs2-in-game-push-notification を選択した際の GS2-InGamePushNotification のゲーム名
        :type notification_game_name: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_notification_game_name(notification_game_name)
        return self

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
        if logging and not isinstance(logging, bool):
            raise TypeError(type(logging))
        self.__logging = logging

    def with_logging(self, logging):
        """
        ログを記録するかを設定
        :param logging: ログを記録するか
        :type logging: bool
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_logging(logging)
        return self

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
        if logging_date and not isinstance(logging_date, int):
            raise TypeError(type(logging_date))
        self.__logging_date = logging_date

    def with_logging_date(self, logging_date):
        """
        ログを記録する日数を設定
        :param logging_date: ログを記録する日数
        :type logging_date: int
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_logging_date(logging_date)
        return self

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
        if create_room_trigger_script and not isinstance(create_room_trigger_script, unicode):
            raise TypeError(type(create_room_trigger_script))
        self.__create_room_trigger_script = create_room_trigger_script

    def with_create_room_trigger_script(self, create_room_trigger_script):
        """
        ルーム作成時 に実行されるGS2-Scriptを設定
        :param create_room_trigger_script: ルーム作成時 に実行されるGS2-Script
        :type create_room_trigger_script: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_create_room_trigger_script(create_room_trigger_script)
        return self

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
        if create_room_done_trigger_script and not isinstance(create_room_done_trigger_script, unicode):
            raise TypeError(type(create_room_done_trigger_script))
        self.__create_room_done_trigger_script = create_room_done_trigger_script

    def with_create_room_done_trigger_script(self, create_room_done_trigger_script):
        """
        ルーム作成完了時 に実行されるGS2-Scriptを設定
        :param create_room_done_trigger_script: ルーム作成完了時 に実行されるGS2-Script
        :type create_room_done_trigger_script: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_create_room_done_trigger_script(create_room_done_trigger_script)
        return self

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
        if delete_room_trigger_script and not isinstance(delete_room_trigger_script, unicode):
            raise TypeError(type(delete_room_trigger_script))
        self.__delete_room_trigger_script = delete_room_trigger_script

    def with_delete_room_trigger_script(self, delete_room_trigger_script):
        """
        ルーム削除時 に実行されるGS2-Scriptを設定
        :param delete_room_trigger_script: ルーム削除時 に実行されるGS2-Script
        :type delete_room_trigger_script: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_delete_room_trigger_script(delete_room_trigger_script)
        return self

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
        if delete_room_done_trigger_script and not isinstance(delete_room_done_trigger_script, unicode):
            raise TypeError(type(delete_room_done_trigger_script))
        self.__delete_room_done_trigger_script = delete_room_done_trigger_script

    def with_delete_room_done_trigger_script(self, delete_room_done_trigger_script):
        """
        ルーム削除完了時 に実行されるGS2-Scriptを設定
        :param delete_room_done_trigger_script: ルーム削除完了時 に実行されるGS2-Script
        :type delete_room_done_trigger_script: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_delete_room_done_trigger_script(delete_room_done_trigger_script)
        return self

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
        if create_subscribe_trigger_script and not isinstance(create_subscribe_trigger_script, unicode):
            raise TypeError(type(create_subscribe_trigger_script))
        self.__create_subscribe_trigger_script = create_subscribe_trigger_script

    def with_create_subscribe_trigger_script(self, create_subscribe_trigger_script):
        """
        ルーム購読時 に実行されるGS2-Scriptを設定
        :param create_subscribe_trigger_script: ルーム購読時 に実行されるGS2-Script
        :type create_subscribe_trigger_script: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_create_subscribe_trigger_script(create_subscribe_trigger_script)
        return self

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
        if create_subscribe_done_trigger_script and not isinstance(create_subscribe_done_trigger_script, unicode):
            raise TypeError(type(create_subscribe_done_trigger_script))
        self.__create_subscribe_done_trigger_script = create_subscribe_done_trigger_script

    def with_create_subscribe_done_trigger_script(self, create_subscribe_done_trigger_script):
        """
        ルーム購読完了時 に実行されるGS2-Scriptを設定
        :param create_subscribe_done_trigger_script: ルーム購読完了時 に実行されるGS2-Script
        :type create_subscribe_done_trigger_script: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_create_subscribe_done_trigger_script(create_subscribe_done_trigger_script)
        return self

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
        if delete_subscribe_trigger_script and not isinstance(delete_subscribe_trigger_script, unicode):
            raise TypeError(type(delete_subscribe_trigger_script))
        self.__delete_subscribe_trigger_script = delete_subscribe_trigger_script

    def with_delete_subscribe_trigger_script(self, delete_subscribe_trigger_script):
        """
        ルーム購読解除時 に実行されるGS2-Scriptを設定
        :param delete_subscribe_trigger_script: ルーム購読解除時 に実行されるGS2-Script
        :type delete_subscribe_trigger_script: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_delete_subscribe_trigger_script(delete_subscribe_trigger_script)
        return self

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
        if delete_subscribe_done_trigger_script and not isinstance(delete_subscribe_done_trigger_script, unicode):
            raise TypeError(type(delete_subscribe_done_trigger_script))
        self.__delete_subscribe_done_trigger_script = delete_subscribe_done_trigger_script

    def with_delete_subscribe_done_trigger_script(self, delete_subscribe_done_trigger_script):
        """
        ルーム購読解除完了時 に実行されるGS2-Scriptを設定
        :param delete_subscribe_done_trigger_script: ルーム購読解除完了時 に実行されるGS2-Script
        :type delete_subscribe_done_trigger_script: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_delete_subscribe_done_trigger_script(delete_subscribe_done_trigger_script)
        return self

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
        if send_message_trigger_script and not isinstance(send_message_trigger_script, unicode):
            raise TypeError(type(send_message_trigger_script))
        self.__send_message_trigger_script = send_message_trigger_script

    def with_send_message_trigger_script(self, send_message_trigger_script):
        """
        メッセージ送信時 に実行されるGS2-Scriptを設定
        :param send_message_trigger_script: メッセージ送信時 に実行されるGS2-Script
        :type send_message_trigger_script: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_send_message_trigger_script(send_message_trigger_script)
        return self

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
        if send_message_done_trigger_script and not isinstance(send_message_done_trigger_script, unicode):
            raise TypeError(type(send_message_done_trigger_script))
        self.__send_message_done_trigger_script = send_message_done_trigger_script

    def with_send_message_done_trigger_script(self, send_message_done_trigger_script):
        """
        メッセージ送信完了時 に実行されるGS2-Scriptを設定
        :param send_message_done_trigger_script: メッセージ送信完了時 に実行されるGS2-Script
        :type send_message_done_trigger_script: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_send_message_done_trigger_script(send_message_done_trigger_script)
        return self
