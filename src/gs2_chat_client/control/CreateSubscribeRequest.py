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


class CreateSubscribeRequest(Gs2BasicRequest):

    class Constant(Gs2Chat):
        FUNCTION = "CreateSubscribe"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateSubscribeRequest, self).__init__(params)
        if params is None:
            self.__lobby_name = None
        else:
            self.set_lobby_name(params['lobbyName'] if 'lobbyName' in params.keys() else None)
        if params is None:
            self.__room_id = None
        else:
            self.set_room_id(params['roomId'] if 'roomId' in params.keys() else None)
        if params is None:
            self.__user_id = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
        if params is None:
            self.__enable_offline_transfer = None
        else:
            self.set_enable_offline_transfer(params['enableOfflineTransfer'] if 'enableOfflineTransfer' in params.keys() else None)
        if params is None:
            self.__offline_transfer_sound = None
        else:
            self.set_offline_transfer_sound(params['offlineTransferSound'] if 'offlineTransferSound' in params.keys() else None)
        if params is None:
            self.__password = None
        else:
            self.set_password(params['password'] if 'password' in params.keys() else None)

    def get_lobby_name(self):
        """
        ロビーの名前を取得
        :return: ロビーの名前
        :rtype: unicode
        """
        return self.__lobby_name

    def set_lobby_name(self, lobby_name):
        """
        ロビーの名前を設定
        :param lobby_name: ロビーの名前
        :type lobby_name: unicode
        """
        if lobby_name is not None and not (isinstance(lobby_name, str) or isinstance(lobby_name, unicode)):
            raise TypeError(type(lobby_name))
        self.__lobby_name = lobby_name

    def with_lobby_name(self, lobby_name):
        """
        ロビーの名前を設定
        :param lobby_name: ロビーの名前
        :type lobby_name: unicode
        :return: this
        :rtype: CreateSubscribeRequest
        """
        self.set_lobby_name(lobby_name)
        return self

    def get_room_id(self):
        """
        ルームIDを取得
        :return: ルームID
        :rtype: unicode
        """
        return self.__room_id

    def set_room_id(self, room_id):
        """
        ルームIDを設定
        :param room_id: ルームID
        :type room_id: unicode
        """
        if room_id is not None and not (isinstance(room_id, str) or isinstance(room_id, unicode)):
            raise TypeError(type(room_id))
        self.__room_id = room_id

    def with_room_id(self, room_id):
        """
        ルームIDを設定
        :param room_id: ルームID
        :type room_id: unicode
        :return: this
        :rtype: CreateSubscribeRequest
        """
        self.set_room_id(room_id)
        return self

    def get_user_id(self):
        """
        ユーザIDを取得
        :return: ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        """
        if user_id is not None and not (isinstance(user_id, str) or isinstance(user_id, unicode)):
            raise TypeError(type(user_id))
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        :return: this
        :rtype: CreateSubscribeRequest
        """
        self.set_user_id(user_id)
        return self

    def get_enable_offline_transfer(self):
        """
        GS2-InGamePushNotification 使用時にオフライン転送を使用するかを取得
        :return: GS2-InGamePushNotification 使用時にオフライン転送を使用するか
        :rtype: bool
        """
        return self.__enable_offline_transfer

    def set_enable_offline_transfer(self, enable_offline_transfer):
        """
        GS2-InGamePushNotification 使用時にオフライン転送を使用するかを設定
        :param enable_offline_transfer: GS2-InGamePushNotification 使用時にオフライン転送を使用するか
        :type enable_offline_transfer: bool
        """
        if enable_offline_transfer is not None and not isinstance(enable_offline_transfer, bool):
            raise TypeError(type(enable_offline_transfer))
        self.__enable_offline_transfer = enable_offline_transfer

    def with_enable_offline_transfer(self, enable_offline_transfer):
        """
        GS2-InGamePushNotification 使用時にオフライン転送を使用するかを設定
        :param enable_offline_transfer: GS2-InGamePushNotification 使用時にオフライン転送を使用するか
        :type enable_offline_transfer: bool
        :return: this
        :rtype: CreateSubscribeRequest
        """
        self.set_enable_offline_transfer(enable_offline_transfer)
        return self

    def get_offline_transfer_sound(self):
        """
        GS2-InGamePushNotification 使用時のモバイルプッシュ通知で使用する通知音を取得
        :return: GS2-InGamePushNotification 使用時のモバイルプッシュ通知で使用する通知音
        :rtype: unicode
        """
        return self.__offline_transfer_sound

    def set_offline_transfer_sound(self, offline_transfer_sound):
        """
        GS2-InGamePushNotification 使用時のモバイルプッシュ通知で使用する通知音を設定
        :param offline_transfer_sound: GS2-InGamePushNotification 使用時のモバイルプッシュ通知で使用する通知音
        :type offline_transfer_sound: unicode
        """
        if offline_transfer_sound is not None and not (isinstance(offline_transfer_sound, str) or isinstance(offline_transfer_sound, unicode)):
            raise TypeError(type(offline_transfer_sound))
        self.__offline_transfer_sound = offline_transfer_sound

    def with_offline_transfer_sound(self, offline_transfer_sound):
        """
        GS2-InGamePushNotification 使用時のモバイルプッシュ通知で使用する通知音を設定
        :param offline_transfer_sound: GS2-InGamePushNotification 使用時のモバイルプッシュ通知で使用する通知音
        :type offline_transfer_sound: unicode
        :return: this
        :rtype: CreateSubscribeRequest
        """
        self.set_offline_transfer_sound(offline_transfer_sound)
        return self

    def get_password(self):
        """
        パスワードを取得
        :return: パスワード
        :rtype: unicode
        """
        return self.__password

    def set_password(self, password):
        """
        パスワードを設定
        :param password: パスワード
        :type password: unicode
        """
        if password is not None and not (isinstance(password, str) or isinstance(password, unicode)):
            raise TypeError(type(password))
        self.__password = password

    def with_password(self, password):
        """
        パスワードを設定
        :param password: パスワード
        :type password: unicode
        :return: this
        :rtype: CreateSubscribeRequest
        """
        self.set_password(password)
        return self
