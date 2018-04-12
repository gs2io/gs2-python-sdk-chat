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


class Subscribe(object):

    def __init__(self, params=None):
        if params is None:
            self.__room_id = None
            self.__user_id = None
            self.__enable_offline_transfer = None
            self.__offline_transfer_sound = None
            self.__subscribe_at = None
        else:
            self.set_room_id(params['roomId'] if 'roomId' in params.keys() else None)
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_enable_offline_transfer(params['enableOfflineTransfer'] if 'enableOfflineTransfer' in params.keys() else None)
            self.set_offline_transfer_sound(params['offlineTransferSound'] if 'offlineTransferSound' in params.keys() else None)
            self.set_subscribe_at(params['subscribeAt'] if 'subscribeAt' in params.keys() else None)

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
        self.__room_id = room_id

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
        self.__user_id = user_id

    def get_enable_offline_transfer(self):
        """
        オフライン転送を使用するかを取得
        :return: オフライン転送を使用するか
        :rtype: bool
        """
        return self.__enable_offline_transfer

    def set_enable_offline_transfer(self, enable_offline_transfer):
        """
        オフライン転送を使用するかを設定
        :param enable_offline_transfer: オフライン転送を使用するか
        :type enable_offline_transfer: bool
        """
        self.__enable_offline_transfer = enable_offline_transfer

    def get_offline_transfer_sound(self):
        """
        通知音を取得
        :return: 通知音
        :rtype: unicode
        """
        return self.__offline_transfer_sound

    def set_offline_transfer_sound(self, offline_transfer_sound):
        """
        通知音を設定
        :param offline_transfer_sound: 通知音
        :type offline_transfer_sound: unicode
        """
        self.__offline_transfer_sound = offline_transfer_sound

    def get_subscribe_at(self):
        """
        購読日時(エポック秒)を取得
        :return: 購読日時(エポック秒)
        :rtype: int
        """
        return self.__subscribe_at

    def set_subscribe_at(self, subscribe_at):
        """
        購読日時(エポック秒)を設定
        :param subscribe_at: 購読日時(エポック秒)
        :type subscribe_at: int
        """
        self.__subscribe_at = subscribe_at

    def to_dict(self):
        return {
            "roomId": self.__room_id,
            "userId": self.__user_id,
            "enableOfflineTransfer": self.__enable_offline_transfer,
            "offlineTransferSound": self.__offline_transfer_sound,
            "subscribeAt": self.__subscribe_at,
        }
