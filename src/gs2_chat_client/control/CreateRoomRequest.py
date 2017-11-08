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


class CreateRoomRequest(Gs2BasicRequest):

    class Constant(Gs2Chat):
        FUNCTION = "CreateRoom"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateRoomRequest, self).__init__(params)
        if params is None:
            self.__lobby_name = None
            self.__room_id = None
            self.__password = None
            self.__allow_user_ids = None
        else:
            self.set_lobby_name(params['lobbyName'] if 'lobbyName' in params.keys() else None)
            self.set_room_id(params['roomId'] if 'roomId' in params.keys() else None)
            self.set_password(params['password'] if 'password' in params.keys() else None)
            self.set_allow_user_ids(params['allowUserIds'] if 'allowUserIds' in params.keys() else None)

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
        self.__lobby_name = lobby_name

    def with_lobby_name(self, lobby_name):
        """
        ロビーの名前を設定
        :param lobby_name: ロビーの名前
        :type lobby_name: unicode
        :return: this
        :rtype: CreateRoomRequest
        """
        self.set_lobby_name(lobby_name)
        return self

    def get_room_id(self):
        """
        ルームID（指定しない場合は自動的に採番されます）を取得
        :return: ルームID（指定しない場合は自動的に採番されます）
        :rtype: unicode
        """
        return self.__room_id

    def set_room_id(self, room_id):
        """
        ルームID（指定しない場合は自動的に採番されます）を設定
        :param room_id: ルームID（指定しない場合は自動的に採番されます）
        :type room_id: unicode
        """
        self.__room_id = room_id

    def with_room_id(self, room_id):
        """
        ルームID（指定しない場合は自動的に採番されます）を設定
        :param room_id: ルームID（指定しない場合は自動的に採番されます）
        :type room_id: unicode
        :return: this
        :rtype: CreateRoomRequest
        """
        self.set_room_id(room_id)
        return self

    def get_password(self):
        """
        ルームにアクセスする際にパスワードを要求する場合は文字列を指定を取得
        :return: ルームにアクセスする際にパスワードを要求する場合は文字列を指定
        :rtype: unicode
        """
        return self.__password

    def set_password(self, password):
        """
        ルームにアクセスする際にパスワードを要求する場合は文字列を指定を設定
        :param password: ルームにアクセスする際にパスワードを要求する場合は文字列を指定
        :type password: unicode
        """
        self.__password = password

    def with_password(self, password):
        """
        ルームにアクセスする際にパスワードを要求する場合は文字列を指定を設定
        :param password: ルームにアクセスする際にパスワードを要求する場合は文字列を指定
        :type password: unicode
        :return: this
        :rtype: CreateRoomRequest
        """
        self.set_password(password)
        return self

    def get_allow_user_ids(self):
        """
        ルームへのアクセスを許可するユーザIDリストをカンマ区切りで指定を取得
        :return: ルームへのアクセスを許可するユーザIDリストをカンマ区切りで指定
        :rtype: unicode
        """
        return self.__allow_user_ids

    def set_allow_user_ids(self, allow_user_ids):
        """
        ルームへのアクセスを許可するユーザIDリストをカンマ区切りで指定を設定
        :param allow_user_ids: ルームへのアクセスを許可するユーザIDリストをカンマ区切りで指定
        :type allow_user_ids: unicode
        """
        self.__allow_user_ids = allow_user_ids

    def with_allow_user_ids(self, allow_user_ids):
        """
        ルームへのアクセスを許可するユーザIDリストをカンマ区切りで指定を設定
        :param allow_user_ids: ルームへのアクセスを許可するユーザIDリストをカンマ区切りで指定
        :type allow_user_ids: unicode
        :return: this
        :rtype: CreateRoomRequest
        """
        self.set_allow_user_ids(allow_user_ids)
        return self
