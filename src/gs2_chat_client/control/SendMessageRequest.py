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

from gs2_core_client.Gs2UserRequest import Gs2UserRequest
from gs2_chat_client.Gs2Chat import Gs2Chat


class SendMessageRequest(Gs2UserRequest):

    class Constant(Gs2Chat):
        FUNCTION = "SendMessage"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(SendMessageRequest, self).__init__(params)
        if params is None:
            self.__lobby_name = None
            self.__room_id = None
            self.__message = None
            self.__meta = None
            self.__password = None
        else:
            self.set_lobby_name(params['lobbyName'] if 'lobbyName' in params.keys() else None)
            self.set_room_id(params['roomId'] if 'roomId' in params.keys() else None)
            self.set_message(params['message'] if 'message' in params.keys() else None)
            self.set_meta(params['meta'] if 'meta' in params.keys() else None)
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
        if lobby_name and not isinstance(lobby_name, unicode):
            raise TypeError(type(lobby_name))
        self.__lobby_name = lobby_name

    def with_lobby_name(self, lobby_name):
        """
        ロビーの名前を設定
        :param lobby_name: ロビーの名前
        :type lobby_name: unicode
        :return: this
        :rtype: SendMessageRequest
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
        if room_id and not isinstance(room_id, unicode):
            raise TypeError(type(room_id))
        self.__room_id = room_id

    def with_room_id(self, room_id):
        """
        ルームIDを設定
        :param room_id: ルームID
        :type room_id: unicode
        :return: this
        :rtype: SendMessageRequest
        """
        self.set_room_id(room_id)
        return self

    def get_message(self):
        """
        メッセージテキストを取得
        :return: メッセージテキスト
        :rtype: unicode
        """
        return self.__message

    def set_message(self, message):
        """
        メッセージテキストを設定
        :param message: メッセージテキスト
        :type message: unicode
        """
        if message and not isinstance(message, unicode):
            raise TypeError(type(message))
        self.__message = message

    def with_message(self, message):
        """
        メッセージテキストを設定
        :param message: メッセージテキスト
        :type message: unicode
        :return: this
        :rtype: SendMessageRequest
        """
        self.set_message(message)
        return self

    def get_meta(self):
        """
        メッセージメタデータを取得
        :return: メッセージメタデータ
        :rtype: unicode
        """
        return self.__meta

    def set_meta(self, meta):
        """
        メッセージメタデータを設定
        :param meta: メッセージメタデータ
        :type meta: unicode
        """
        if meta and not isinstance(meta, unicode):
            raise TypeError(type(meta))
        self.__meta = meta

    def with_meta(self, meta):
        """
        メッセージメタデータを設定
        :param meta: メッセージメタデータ
        :type meta: unicode
        :return: this
        :rtype: SendMessageRequest
        """
        self.set_meta(meta)
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
        if password and not isinstance(password, unicode):
            raise TypeError(type(password))
        self.__password = password

    def with_password(self, password):
        """
        パスワードを設定
        :param password: パスワード
        :type password: unicode
        :return: this
        :rtype: SendMessageRequest
        """
        self.set_password(password)
        return self
