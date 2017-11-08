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
            self.__notification_game_name = None
            self.__notification_url = None
            self.__service_class = None
            self.__notification_type = None
            self.__description = None
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_notification_game_name(params['notificationGameName'] if 'notificationGameName' in params.keys() else None)
            self.set_notification_url(params['notificationUrl'] if 'notificationUrl' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_notification_type(params['notificationType'] if 'notificationType' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)

    def get_name(self):
        """
        ロビー名を取得
        :return: ロビー名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        ロビー名を設定
        :param name: ロビー名
        :type name: unicode
        """
        self.__name = name

    def with_name(self, name):
        """
        ロビー名を設定
        :param name: ロビー名
        :type name: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_name(name)
        return self

    def get_notification_game_name(self):
        """
        通知先 GS2-InGamePushNotification の ゲーム名を取得
        :return: 通知先 GS2-InGamePushNotification の ゲーム名
        :rtype: unicode
        """
        return self.__notification_game_name

    def set_notification_game_name(self, notification_game_name):
        """
        通知先 GS2-InGamePushNotification の ゲーム名を設定
        :param notification_game_name: 通知先 GS2-InGamePushNotification の ゲーム名
        :type notification_game_name: unicode
        """
        self.__notification_game_name = notification_game_name

    def with_notification_game_name(self, notification_game_name):
        """
        通知先 GS2-InGamePushNotification の ゲーム名を設定
        :param notification_game_name: 通知先 GS2-InGamePushNotification の ゲーム名
        :type notification_game_name: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_notification_game_name(notification_game_name)
        return self

    def get_notification_url(self):
        """
        通知先URLを取得
        :return: 通知先URL
        :rtype: unicode
        """
        return self.__notification_url

    def set_notification_url(self, notification_url):
        """
        通知先URLを設定
        :param notification_url: 通知先URL
        :type notification_url: unicode
        """
        self.__notification_url = notification_url

    def with_notification_url(self, notification_url):
        """
        通知先URLを設定
        :param notification_url: 通知先URL
        :type notification_url: unicode
        :return: this
        :rtype: CreateLobbyRequest
        """
        self.set_notification_url(notification_url)
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
