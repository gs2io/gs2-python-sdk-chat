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


class DescribeMessageRequest(Gs2UserRequest):

    class Constant(Gs2Chat):
        FUNCTION = "DescribeMessage"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DescribeMessageRequest, self).__init__(params)
        if params is None:
            self.__lobby_name = None
            self.__room_id = None
            self.__password = None
            self.__start_at = None
            self.__limit = None
        else:
            self.set_lobby_name(params['lobbyName'] if 'lobbyName' in params.keys() else None)
            self.set_room_id(params['roomId'] if 'roomId' in params.keys() else None)
            self.set_password(params['password'] if 'password' in params.keys() else None)
            self.set_start_at(params['startAt'] if 'startAt' in params.keys() else None)
            self.set_limit(params['limit'] if 'limit' in params.keys() else None)

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
        if not isinstance(lobby_name, unicode):
            raise TypeError(type(lobby_name))
        self.__lobby_name = lobby_name

    def with_lobby_name(self, lobby_name):
        """
        ロビーの名前を設定
        :param lobby_name: ロビーの名前
        :type lobby_name: unicode
        :return: this
        :rtype: DescribeMessageRequest
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
        if not isinstance(room_id, unicode):
            raise TypeError(type(room_id))
        self.__room_id = room_id

    def with_room_id(self, room_id):
        """
        ルームIDを設定
        :param room_id: ルームID
        :type room_id: unicode
        :return: this
        :rtype: DescribeMessageRequest
        """
        self.set_room_id(room_id)
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
        if not isinstance(password, unicode):
            raise TypeError(type(password))
        self.__password = password

    def with_password(self, password):
        """
        パスワードを設定
        :param password: パスワード
        :type password: unicode
        :return: this
        :rtype: DescribeMessageRequest
        """
        self.set_password(password)
        return self

    def get_start_at(self):
        """
        メッセージの取得を開始する日時(エポック秒)を取得
        :return: メッセージの取得を開始する日時(エポック秒)
        :rtype: int
        """
        return self.__start_at

    def set_start_at(self, start_at):
        """
        メッセージの取得を開始する日時(エポック秒)を設定
        :param start_at: メッセージの取得を開始する日時(エポック秒)
        :type start_at: int
        """
        if not isinstance(start_at, int):
            raise TypeError(type(start_at))
        self.__start_at = start_at

    def with_start_at(self, start_at):
        """
        メッセージの取得を開始する日時(エポック秒)を設定
        :param start_at: メッセージの取得を開始する日時(エポック秒)
        :type start_at: int
        :return: this
        :rtype: DescribeMessageRequest
        """
        self.set_start_at(start_at)
        return self

    def get_limit(self):
        """
        データの取得件数を取得
        :return: データの取得件数
        :rtype: int
        """
        return self.__limit

    def set_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        """
        if not isinstance(limit, int):
            raise TypeError(type(limit))
        self.__limit = limit

    def with_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        :return: this
        :rtype: DescribeMessageRequest
        """
        self.set_limit(limit)
        return self
