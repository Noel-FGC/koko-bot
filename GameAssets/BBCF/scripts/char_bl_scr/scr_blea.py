@State
def EMB():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(300000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_BL.DIG', '')
        RenderLayer(5)
        Size(1200)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4278190335, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4294967295, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 80)


@State
def EMB_BL_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(300000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_BL.DIG', '')
        RenderLayer(5)
        Size(1200)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294967295, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    sprite('null', 80)


@State
def EMB_BL_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(300000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_BL.DIG', '')
        RenderLayer(5)
        Size(1200)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294901760, 10)
    sprite('null', 10)
    ColorTransition(4294912040, 10)
    sprite('null', 10)
    ColorTransition(4294948020, 10)
    sprite('null', 10)
    ColorTransition(4294901760, 10)
    sprite('null', 80)


@State
def BLEF_LockOnZone():

    def upon_IMMEDIATE():
        AddY(300000)
        Eff3DEffect('blef_circle.DIG', '')
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        TurnAround()
        SetActionMark(0)
        CopyFromRightToLeft(23, 2, 51, 3, 2, 23)
        if SLOT_51:
            SLOT_4 = 1000
        else:
            SLOT_4 = 1800

        def upon_EVERY_FRAME():
            if SLOT_2:
                if SLOT_51:
                    SLOT_4 = SLOT_4 + 8
                else:
                    SLOT_4 = SLOT_4 + 11
                CallPrivateFunction('BulletLockOnZone', 2, 4, 0, 0, 0, 0, 0, 0)

        def upon_PLAYER_DAMAGED():
            clearUponHandler(PLAYER_DAMAGED)
            clearUponHandler(32)
            sendToLabel(2)

        def upon_32():
            clearUponHandler(PLAYER_DAMAGED)
            clearUponHandler(32)
            sendToLabel(2)
        EffectPosition(3, 103)
        Unknown23144(3, 0, 103, 0, 0, 0, 0, 0, 50, 0, 20)
    if SLOT_51:
        sendToLabel(100)
    sprite('null', 5)
    Size(0)
    AlphaValue(0)
    ConstantAlphaModifier(60)
    SetScaleSpeed(360)
    sprite('null', 1)
    PrivateSE('blse_01')
    ConstantAlphaModifier(0)
    Size(1800)
    SetScaleSpeed(0)
    gotoLabel(0)
    label(100)
    sprite('null', 5)
    Size(0)
    AlphaValue(0)
    ConstantAlphaModifier(60)
    SetScaleSpeed(200)
    sprite('null', 1)
    PrivateSE('blse_01')
    ConstantAlphaModifier(0)
    Size(1000)
    SetScaleSpeed(0)
    gotoLabel(0)
    label(0)
    sprite('null', 10)
    SetActionMark(1)
    physicsYImpulse(-300)
    sprite('null', 30)
    physicsYImpulse(-200)
    sprite('null', 30)
    physicsYImpulse(-100)
    sprite('null', 10)
    YAccel(0)
    sprite('null', 10)
    physicsYImpulse(300)
    sprite('null', 30)
    physicsYImpulse(200)
    sprite('null', 30)
    physicsYImpulse(100)
    sprite('null', 10)
    YAccel(0)
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('null', 10)
    SetActionMark(0)
    SetScaleSpeed(0)
    ConstantAlphaModifier(-26)


@State
def BLEF_LockOnMarker():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Add()
        Size(500)
        AddRotationPerFrame(-1500)
        SetZVal(-500)
        TeleportToObject(22)
        AddY(200000)
        uponSendToLabel(32, 10)
        uponSendToLabel(33, 20)

        def upon_16():
            PrivateFunction3(22, 0, 0, 60, 1)
    label(0)
    sprite('blef_target', 32767)
    SetScaleSpeed(0)
    label(10)
    sprite('blef_target', 5)
    clearUponHandler(32)
    SetScaleSpeed(60)
    GreenColorValue(31)
    sprite('blef_target', 10)
    PrivateSE('blse_02')
    SetScaleSpeed(-35)
    gotoLabel(0)
    label(20)
    sprite('blef_target', 16)
    clearUponHandler(32)
    clearUponHandler(33)
    clearUponHandler(16)
    SetScaleSpeed(200)
    ConstantAlphaModifier(-16)


@State
def blef405Atk():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        AttackP2(72)
        SameMoveProration(10)
        UseFireHitspark(1)
        IgnoreComboTime(0)
        AirUntechableTime(17)
        Hitstun(17)
        DamageEffect(5, '')
        if SLOT_5 == 1:
            AttackLevel_(4)
            Damage(1500)
            AttackP2(72)
            Hitstop(10)
            AirUntechableTime(35)
            WallstickDuration(27)
            AirHitstunAfterWallbounce(45)
            AirPushbackX(40000)
            AirPushbackY(30000)
            AirHitstunAnimation(13)
            GroundedHitstunAnimation(13)
            Wallbounce(1)
            WallbounceReboundTime(5)
            Wallstick(1)

            def upon_OPPONENT_HIT():
                ScreenShake(15000, 15000)
                CommonSE('100_hit_grap_3')
                PrivateSE('blse_05')
        if SLOT_5 == 2:
            AttackLevel_(5)
            Damage(3350)
            AttackP2(74)
            Hitstop(15)
            AirUntechableTime(40)
            WallstickDuration(45)
            AirHitstunAfterWallbounce(45)
            AirPushbackX(50000)
            AirPushbackY(31250)
            AirHitstunAnimation(19)
            GroundedHitstunAnimation(19)
            Wallbounce(1)
            WallbounceReboundTime(4)
            Wallstick(1)
            if SLOT_OverdriveTimer:
                WallbounceReboundTime(40)

            def upon_OPPONENT_HIT():
                ScreenShake(30000, 0)
                CommonSE('100_hit_grap_3')
                PrivateSE('blse_06')

        def upon_32():
            AddX(330000)
            AddY(250000)
    sprite('vrblef405_test', 3)


@State
def __202_Blast00():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
    sprite('null', 60)
    LinkParticle('blef_5C_start')


@State
def __202_Blast01():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    sprite('null', 60)
    LinkParticle('blef_5C')
    CreateParticle('blef_5C_add', 100)


@State
def shot_charge():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
    sprite('null', 64)
    LinkParticle('blef_charge')


@State
def shot_fire():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        PaletteIndex(1)
        BlendMode_Add()
        AddX(272000)
    sprite('vrblef401_00', 2)
    CreateParticle('blef_shot_blast', 0)
    sprite('vrblef401_01', 2)
    sprite('vrblef401_02', 2)
    sprite('vrblef401_03', 2)
    sprite('vrblef401_04', 2)


@State
def shot_mazzle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        RotationAngle(135000)
    sprite('null', 60)
    LinkParticle('blef_shot_mazzle')


@State
def shot():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        AttackLevel_(3)
        Damage(700)
        AttackP1(80)
        SingleProration(1)
        SameMoveProration(10)
        Hitstop(2)
        EnemyHitstopAddition(6, 6, 8)
        AttackDirection(2)
        UseFireHitspark(1)
        AirUntechableTime(22)
        Hitstun(22)
        CollideWithWall(1)
        StarterRating(2)
        BlendMode_Add()
        PaletteIndex(1)
        SetZVal(-500)
        AddX(64000)
        Size(1500)
        physicsXImpulse(15000)
        SetActionMark(8)
        SLOT_51 = 1

        def upon_32():
            AirPushbackY(25000)
            EnemyHitstopAddition(5, 4, 6)
            SLOT_51 = 2
            clearUponHandler(32)

        def upon_33():
            AirPushbackY(24000)
            EnemyHitstopAddition(3, 2, 4)
            SLOT_51 = 3
            clearUponHandler(33)

        def upon_OPPONENT_HIT_OR_BLOCK():
            if SLOT_52 >= 1:
                Damage(350)
            SLOT_52 = SLOT_52 + 1
            XImpulseAcceleration(75)
            SLOT_51 = SLOT_51 + -1
            if SLOT_51 <= 0:
                clearUponHandler(OPPONENT_HIT_OR_BLOCK)
                SetActionMark(0)
                physicsXImpulse(10000)
                sendToLabel(1)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('null', 5)
    CreateObject('shot_add', -1)
    label(0)
    sprite('vrblef401_10', 2)
    RefreshMultihit()
    PrivateSE('blse_08')
    sprite('vrblef401_11', 2)
    RefreshMultihit()
    sprite('vrblef401_12', 2)
    RefreshMultihit()
    sprite('vrblef401_13', 2)
    RefreshMultihit()
    sprite('vrblef401_14', 2)
    RefreshMultihit()
    sprite('vrblef401_15', 2)
    RefreshMultihit()
    AddActionMark(-1)
    AddAcceleration(50)
    gotoLabel(0)
    label(1)
    sprite('vrblef401_20', 2)
    sprite('vrblef401_21', 2)
    sprite('vrblef401_22', 2)
    sprite('vrblef401_23', 2)


@State
def shot_add():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        AddX(96000)
    label(0)
    sprite('null', 3)
    CreateParticle('blef_shot_add', -1)
    gotoLabel(0)


@State
def shot_geyser():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        BlendMode_Add()
        SetZVal(-500)
        AttackDirection(2)
        AttackLevel_(4)
        Damage(900)
        AttackP1(80)
        SingleProration(1)
        SameMoveProration(10)
        Hitstop(0)
        UseFireHitspark(1)
        EnemyHitstopAddition(18, 18, 20)
        StarterRating(2)
        if SLOT_137:
            DamageMultiplier(80)
        SetActionMark(0)

        def upon_32():
            SetActionMark(1)
            uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 200)
            AddX(74000)
            Size(1300)
            physicsXImpulse(20000)
            Damage(700)
            AirHitstunAnimation(9)
            GroundedHitstunAnimation(9)
            EnemyHitstopAddition(8, 8, 10)
            AirUntechableTime(22)
            Hitstun(22)
            CollideWithWall(1)
            if SLOT_137:
                DamageMultiplier(80)
            physicsXImpulse(12000)
            clearUponHandler(32)
            sendToLabel(99)

        def upon_33():
            SetActionMark(2)
            uponSendToLabel(OPPONENT_HIT_OR_BLOCK, 200)
            AddX(74000)
            Size(1300)
            physicsXImpulse(20000)
            Damage(800)
            AirHitstunAnimation(9)
            GroundedHitstunAnimation(9)
            EnemyHitstopAddition(8, 8, 10)
            AirUntechableTime(22)
            Hitstun(22)
            CollideWithWall(1)
            if SLOT_137:
                DamageMultiplier(80)
            physicsXImpulse(15000)
            clearUponHandler(33)
            sendToLabel(99)
    sprite('null', 1)
    label(999)
    sprite('vrblef401_50', 3)
    RefreshMultihit()
    Size(1000)
    physicsXImpulse(0)
    SetAcceleration(0)
    Hitstun(25)
    AirUntechableTime(38)
    AirPushbackX(0)
    AirPushbackY(35000)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    PushbackX(15000)
    AddX(240000)
    PrivateSE('blse_05')
    sprite('vrblef401_51', 3)
    sprite('vrblef401_52', 3)
    sprite('vrblef401_53', 3)
    sprite('vrblef401_54', 3)
    sprite('vrblef401_55', 3)
    ExitState()
    label(99)
    sprite('vrblef401_10', 1)
    CreateObject('shot_add', -1)
    label(0)
    sprite('vrblef401_10', 2)
    PrivateSE('blse_08')
    sprite('vrblef401_11', 2)
    sprite('vrblef401_12', 2)
    sprite('vrblef401_13', 2)
    sprite('vrblef401_14', 2)
    if SLOT_2 == 0:
        physicsXImpulse(2000)
        sendToLabel(1)
    else:
        AddActionMark(-1)
        AddAcceleration(-400)
    gotoLabel(0)
    label(1)
    sprite('vrblef401_20', 2)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    sprite('keep', 2)
    AddX(-60000)
    sendToLabel(999)
    label(200)
    sprite('vrblef401_20', 2)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    physicsXImpulse(2000)
    EnemyHitstopAddition(14, 14, 16)
    sprite('keep', 2)
    AddX(-120000)
    sendToLabel(999)


@State
def shot_geyser_col():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
    sprite('vrblef401_geyser_col', 15)


@State
def shot_geyser_2():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        BlendMode_Add()
        SetZVal(-500)
        SetScaleX(-1000)
        SetScaleY(750)
        AddX(-128000)
    sprite('vrblef401_50', 3)
    sprite('vrblef401_51', 3)
    sprite('vrblef401_52', 3)
    sprite('vrblef401_53', 3)
    sprite('vrblef401_54', 3)
    sprite('vrblef401_55', 3)


@State
def shot_geyser_3():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        BlendMode_Add()
        SetZVal(-500)
        RotationAngle(45000)
        Size(875)
    sprite('vrblef401_50', 3)
    sprite('vrblef401_51', 3)
    sprite('vrblef401_52', 3)
    sprite('vrblef401_53', 3)
    sprite('vrblef401_54', 3)
    sprite('vrblef401_55', 3)


@State
def shot_geyser_4():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        BlendMode_Add()
        SetZVal(-500)
        RotationAngle(-60000)
    sprite('vrblef401_50', 3)
    sprite('vrblef401_51', 3)
    sprite('vrblef401_52', 3)
    sprite('vrblef401_53', 3)
    sprite('vrblef401_54', 3)
    sprite('vrblef401_55', 3)


@State
def shot_geyser_3d():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_400blast_00.DIG', '')
        FaceSpawnLocation()
        Size(500)
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        RotationAngle(30000)
    sprite('null', 8)
    sprite('null', 8)
    ConstantAlphaModifier(-32)


@State
def __400_mazzle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        DespawnEAEffect('shot_charge')
        Size(750)
    sprite('null', 60)
    LinkParticle('blef_DashThrow_fire')


@State
def __400_mazzle2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        Eff3DEffect('bl_430bom_00.DIG', '')
        FaceSpawnLocation()
        SetScaleY(375)
        SetScaleX(937)
        RotationAngle(100000)
    sprite('null', 10)
    SetScaleSpeed(30)


@State
def __403_mazzle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
    sprite('null', 60)
    CreateObject('403_firewave00', 0)
    CreateParticle('blef_GraspThrow_fire', 0)


@State
def __403_firewave00():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_403firewave_00.DIG', '')
        FaceSpawnLocation()
        Size(750)
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
    sprite('null', 8)
    sprite('null', 8)
    ConstantAlphaModifier(-32)


@State
def __404_mazzle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Size(800)
        DespawnEAEffect('shot_charge')
    sprite('null', 60)
    LinkParticle('blef_DashThrow_fire')


@State
def __404_mazzle2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        Eff3DEffect('bl_430bom_00.DIG', '')
        FaceSpawnLocation()
        SetScaleY(400)
        SetScaleX(1000)
        RotationAngle(100000)
    sprite('null', 10)
    SetScaleSpeed(30)


@State
def __405_mazzle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        DespawnEAEffect('shot_charge')
    sprite('null', 60)
    LinkParticle('blef_GuardCrush')


@State
def blef_410_fire():

    def upon_IMMEDIATE():
        Flip()
        RemoveOnCallStateEnd(2)
        AbsoluteY(0)
        AddX(-50000)
    sprite('null', 4)
    ParticleSize(2000)
    CallCustomizableParticle('blef_410fire', -1)
    sprite('null', 4)
    ParticleSize(2000)
    CallCustomizableParticle('blef_410fire', -1)


@State
def blef_410_finish():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    ParticleRotationAngle(-60000)
    CallCustomizableParticle('blef_410finish', -1)


@State
def __430_handaura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        Size(1500)
    sprite('null', 300)
    SetScaleSpeed(-25)
    LinkParticle('blef_430tame_pos')


@State
def __430_handaura2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        Size(1000)
    sprite('null', 300)
    LinkParticle('blef_430tame_pos')


@State
def __430_mazzle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        Eff3DEffect('bl_430bom_00.DIG', '')
        FaceSpawnLocation()
        Size(800)
        RotationAngle(30000)
    sprite('null', 10)
    PrivateSE('blse_05')
    ParticleRotationAngle(-45000)
    CallCustomizableParticle('blef_430atk_hinoko', -1)
    SetScaleSpeed(30)


@State
def __430_mazzle2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        Eff3DEffect('bl_430bom_01.DIG', '')
        FaceSpawnLocation()
        Size(600)
        RotationAngle(30000)
    sprite('null', 10)
    PrivateSE('blse_05')
    ParticleRotationAngle(-45000)
    CallCustomizableParticle('blef_430atk_circle', -1)
    SetScaleSpeed(30)


@State
def __430_mazzlelast():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        Size(900)
        RotationAngle(30000)
    sprite('null', 2)
    PrivateSE('blse_06')
    sprite('null', 4)
    Eff3DEffect('bl_430bom_01.DIG', '')
    FaceSpawnLocation()
    ParticleRotationAngle(130000)
    CallCustomizableParticle('blef_433bloom_add2', -1)
    SetScaleSpeed(30)
    sprite('null', 7)


@State
def __430_bigmazzleShockDown():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        Eff3DEffect('bl_430bom_01.DIG', '')
        FaceSpawnLocation()
        Size(400)
        RotationAngle(30000)
    sprite('null', 10)
    ParticleRotationAngle(-45000)
    CallCustomizableParticle('blef_430atk_circle', -1)
    SetScaleSpeed(30)


@State
def __430_bigmazzleFireMatoDown():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
    sprite('null', 5)
    CreateObject('430_bigmazzleFire2Down', -1)


@State
def __430_bigmazzleFire2Down():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AlphaValue(255)
        Eff3DEffect('bl_433fire_00', '')
        FaceSpawnLocation()
        RotationAngle(-60000)
    sprite('null', 11)
    sprite('null', 4)
    ConstantAlphaModifier(-61)


@State
def __430_ShockCircleDown():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450firecircle_00.DIG', '')
        FaceSpawnLocation()
        RotationAngle(-60000)
        AddY(-150000)
        AddX(-70000)
        Size(1000)
        AlphaValue(150)
    sprite('null', 14)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __431_mazzle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RotationAngle(30000)
    sprite('null', 60)
    LinkParticle('blef_DD_fire')


@State
def __431_bigmazzleShockmatome():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
    sprite('null', 2)
    CreateParticle('blef_433bloom_add2', -1)
    CreateObject('431_bigmazzleShock', -1)
    sprite('null', 10)
    CreateObject('431_bigmazzleFireMato', -1)
    sprite('null', 3)
    CreateObject('431_ShockCircle', -1)


@State
def __431_bigmazzleShock():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450atkshot_01.DIG', '')
        FaceSpawnLocation()
        RotationAngle(180000)
        Size(1208)
    sprite('null', 7)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __431_bigmazzleFireMato():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
    sprite('null', 5)
    CreateObject('431_bigmazzleFire', -1)
    sprite('null', 5)
    CreateObject('431_bigmazzleFire', -1)


@State
def __431_bigmazzleFire():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450atkfire_01', '')
        FaceSpawnLocation()
        PaletteIndex(1)
        ColorFromPaletteIndex(243)
        RotationAngle(-100000)
        Size(800)
    sprite('null', 3)
    CreateObject('431_bigmazzleFire2', -1)
    SetScaleXPerFrame(-15)
    sprite('null', 8)
    sprite('null', 4)
    physicsYImpulse(1500)


@State
def __431_bigmazzleFire2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(243)
        IgnoreScreenfreeze(1)
        AlphaValue(255)
        Eff3DEffect('bl_433fire_00', '')
        FaceSpawnLocation()
        RotationAngle(-90000)
    sprite('null', 8)
    sprite('null', 4)
    ConstantAlphaModifier(-61)


@State
def __431_ShockCircle():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450firecircle_00.DIG', '')
        FaceSpawnLocation()
        AddX(-200000)
        Size(1200)
    sprite('null', 14)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __431_bigmazzleShockmatomeDown():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        AddY(150000)
    sprite('null', 2)
    ParticleRotationAngle(90000)
    CallCustomizableParticle('blef_433bloom_add2', -1)
    CreateObject('431_bigmazzleShockDown', -1)
    ParticleRotationAngle(-90000)
    ParticleSize(800)
    CallCustomizableParticle('blef_433hibana_add2', -1)
    sprite('null', 5)
    CreateObject('431_bigmazzleFireMatoDown', -1)
    sprite('null', 3)
    CreateObject('431_ShockCircleDown', -1)


@State
def __431_bigmazzleShockDown():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450atkshot_01.DIG', '')
        FaceSpawnLocation()
        RotationAngle(90000)
        Size(1057)
    sprite('null', 7)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __431_bigmazzleFireMatoDown():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
    sprite('null', 5)
    CreateObject('431_bigmazzleFire2Down', -1)
    sprite('null', 5)
    CreateObject('431_bigmazzleFire2Down', -1)


@State
def __431_bigmazzleFire2Down():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(243)
        IgnoreScreenfreeze(1)
        AlphaValue(255)
        Eff3DEffect('bl_433fire_00', '')
        FaceSpawnLocation()
        RotationAngle(900000)
        SetScaleX(1500)
    sprite('null', 8)
    sprite('null', 4)
    ConstantAlphaModifier(-61)


@State
def __431_ShockCircleDown():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450firecircle_00.DIG', '')
        FaceSpawnLocation()
        RotationAngle(94000)
        AddY(-50000)
        Size(1400)
        AlphaValue(150)
    sprite('null', 14)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __431_bigmazzleShockmatomeUp():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        AddY(150000)
    sprite('null', 2)
    ParticleRotationAngle(-90000)
    CallCustomizableParticle('blef_433bloom_add2', -1)
    CreateObject('431_bigmazzleShockUp', -1)
    sprite('null', 5)
    ParticleRotationAngle(90000)
    ParticleSize(800)
    CallCustomizableParticle('blef_433hibana_add2', -1)
    CreateObject('431_bigmazzleFireMatoUp', -1)
    CreateObject('431_ShockCircleUp', -1)


@State
def __431_bigmazzleShockUp():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450atkshot_01.DIG', '')
        FaceSpawnLocation()
        RotationAngle(90000)
        Size(1208)
    sprite('null', 7)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __431_bigmazzleFireMatoUp():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
    sprite('null', 5)
    CreateObject('431_bigmazzleFire2Up', -1)
    sprite('null', 5)
    CreateObject('431_bigmazzleFire2Up', -1)


@State
def __431_bigmazzleFire2Up():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(243)
        IgnoreScreenfreeze(1)
        AlphaValue(255)
        Eff3DEffect('bl_433fire_00', '')
        FaceSpawnLocation()
        SetScaleX(1500)
        AddY(-200000)
        Rotation(10000)
    sprite('null', 8)
    sprite('null', 4)
    ConstantAlphaModifier(-61)


@State
def __431_ShockCircleUp():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450firecircle_00.DIG', '')
        FaceSpawnLocation()
        RotationAngle(-88000)
        AddY(-50000)
        Size(1600)
        AlphaValue(150)
    sprite('null', 14)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def blef_entry():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
    sprite('vrblef601_00', 3)
    sprite('vrblef601_01', 3)
    sprite('vrblef601_02', 3)


@State
def __408_BodyFire():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(1)
        RenderLayer(2)
        LinkParticle('blef_408tamefire_tubu')
        RemoveOnCallStateEnd(2)
    sprite('null', 30)
    sprite('null', 10)


@State
def __408_Fireroop():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 10)
    CreateObject('408_Fire', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 16)


@State
def __408_Fire():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450tamefire_00.DIG', '')
        FaceSpawnLocation()
        Size(700)
        AlphaValue(200)
    sprite('null', 10)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __408_Kaiho():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        SetScaleY(2000)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 5)
    CreateObject('408_Kaiho00', -1)
    CreateParticle('blef_450tame_tubu', -1)
    sprite('null', 5)
    CreateObject('408_Kaiho01', -1)
    sprite('null', 5)
    CreateObject('408_Kaiho02', -1)


@State
def __408_Kaiho00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AlphaValue(255)
        PaletteIndex(1)
        ColorFromPaletteIndex(243)
        Eff3DEffect('bl_450smoke_00', '')
        FaceSpawnLocation()
        SetScaleX(1300)
    sprite('null', 11)
    SetScaleXPerFrame(-5)
    sprite('null', 4)
    physicsYImpulse(1500)


@State
def __408_Kaiho01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AlphaValue(255)
        PaletteIndex(1)
        ColorFromPaletteIndex(243)
        Eff3DEffect('bl_450smoke_00', '')
        FaceSpawnLocation()
        AddX(70000)
        SetScaleY(500)
        RotationAngle(5000)
    sprite('null', 11)
    SetScaleXPerFrame(-5)
    sprite('null', 4)
    physicsYImpulse(1500)


@State
def __408_Kaiho02():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        ColorFromPaletteIndex(243)
        AlphaValue(255)
        Size(1000)
        Flip()
        Eff3DEffect('bl_450smoke_00', '')
        FaceSpawnLocation()
        AddX(70000)
        SetScaleY(500)
        RotationAngle(5000)
    sprite('null', 11)
    SetScaleXPerFrame(-5)
    sprite('null', 4)
    physicsYImpulse(1000)


@State
def __450_gandredfireroop():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 10)
    CreateObject('450_gandredfire', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)


@State
def __450_gandredfire():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450tamefire_00.DIG', '')
        FaceSpawnLocation()
        Size(800)
    sprite('null', 10)
    SetScaleSpeedY(10)
    SetScaleXPerFrame(-10)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __450_Zanzo():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        RenderLayer(1)
    sprite('vrbl450_00', 3)
    CreateParticle('blef_450atk1_sub', 0)
    CreateParticle('blef_450atk1_sub', 1)
    sprite('vrbl450_01', 4)
    CreateParticle('blef_450atk1_sub', 0)
    CreateParticle('blef_450atk1_sub', 1)
    sprite('vrbl450_02', 4)
    CreateParticle('blef_450atk1_sub', 0)
    CreateParticle('blef_450atk1_sub', 1)
    ConstantAlphaModifier(-51)


@State
def __450_tamesmokeroop():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        SetScaleY(2000)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 5)
    CreateObject('450_tamesmoke00', -1)
    ParticleSize(1300)
    CallCustomizableParticle('blef_450tame_tubu', -1)
    sprite('null', 5)
    CreateObject('450_tamesmoke01', -1)
    sprite('null', 5)
    CreateObject('450_tamesmoke02', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 20)


@State
def __450_tamesmoke00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AlphaValue(200)
        Eff3DEffect('bl_450smoke_00', '')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(2)
        SetScaleX(1400)
    sprite('null', 11)
    SetScaleXPerFrame(-5)
    sprite('null', 4)
    physicsYImpulse(1500)


@State
def __450_tamesmoke01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AlphaValue(200)
        Eff3DEffect('bl_450smoke_00', '')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(2)
        AddX(70000)
        SetScaleY(600)
        SetScaleX(1400)
    sprite('null', 11)
    SetScaleXPerFrame(-5)
    sprite('null', 4)
    physicsYImpulse(1500)


@State
def __450_tamesmoke02():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AlphaValue(200)
        Size(1000)
        Eff3DEffect('bl_450smoke_00', '')
        FaceSpawnLocation()
        RemoveOnCallStateEnd(2)
        AddX(-70000)
        SetScaleY(700)
        SetScaleX(1400)
    sprite('null', 11)
    SetScaleXPerFrame(-5)
    sprite('null', 4)
    physicsYImpulse(1500)


@State
def __450_bigmazzle00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450atkshot_00.DIG', '')
        FaceSpawnLocation()
        RotationAngle(45000)
        SetScaleY(1200)
    sprite('null', 4)
    CreateObject('450_bigmazzleFire', -1)
    CreateObject('450_fire', -1)
    CreateObject('450_bigmazzleShock', -1)
    AddScale(-300)
    sprite('null', 12)
    ParticleRotationAngle(45000)
    CallCustomizableParticle('blef_450atk2_circle', -1)
    AddScale(300)
    sprite('null', 3)
    ConstantAlphaModifier(-51)


@State
def __450_bigmazzle01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450atkshot_00.DIG', '')
        FaceSpawnLocation()
        RotationAngle(45000)
        Size(1300)
    sprite('null', 4)
    CreateObject('450_bigmazzleFire', -1)
    CreateObject('450_fire', -1)
    CreateObject('450_bigmazzleShock', -1)
    AddScale(-300)
    sprite('null', 12)
    ParticleRotationAngle(45000)
    CallCustomizableParticle('blef_450atk2_circle', -1)
    AddScale(300)
    sprite('null', 3)
    ConstantAlphaModifier(-51)


@State
def __450_bigmazzle02():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450atkshot_00.DIG', '')
        FaceSpawnLocation()
        RotationAngle(45000)
        Size(1400)
    sprite('null', 4)
    CreateObject('450_bigmazzleFire', -1)
    CreateObject('450_fire', -1)
    CreateObject('450_bigmazzleShock', -1)
    AddScale(-300)
    sprite('null', 12)
    ParticleRotationAngle(45000)
    CallCustomizableParticle('blef_450atk2_circle', -1)
    AddScale(300)
    sprite('null', 3)
    ConstantAlphaModifier(-51)


@State
def __450_bigmazzleShock():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450atkshot_01.DIG', '')
        FaceSpawnLocation()
        RotationAngle(45000)
    sprite('null', 5)
    SetScaleSpeed(50)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __450_bigmazzleShock2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450firecircle_00.DIG', '')
        FaceSpawnLocation()
        RotationAngle(95000)
        Size(1500)
        AddX(-40000)
    sprite('null', 14)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __450_bigmazzleFire():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450atkfire_01', '')
        FaceSpawnLocation()
        RotationAngle(-45000)
    sprite('null', 11)
    SetScaleXPerFrame(-15)
    sprite('null', 4)
    physicsYImpulse(1500)


@State
def __450_fire():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450atkfire_00.DIG', '')
        FaceSpawnLocation()
        RotationAngle(45000)
        AlphaValue(0)
    sprite('null', 15)
    ConstantAlphaModifier(51)
    SetScaleSpeedY(-30)
    sprite('null', 15)
    ConstantAlphaModifier(-17)


@State
def __450_ryuhai():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450ryuhai_00', '')
        FaceSpawnLocation()
        E0EAEffectPosition(2)
        uponSendToLabel(32, 0)
        AlphaValue(0)
    sprite('null', 10)
    ConstantAlphaModifier(26)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def __450_lastAtk00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450lastatk_00.DIG', '')
        FaceSpawnLocation()
        Size(1000)
    sprite('null', 7)
    CreateParticle('blef_450lastground_pos', -1)
    SetScaleSpeed(20)
    sprite('null', 6)
    ConstantAlphaModifier(-51)
    CreateObject('450_lastAtkrenzoku', -1)


@State
def __450_lastAtk01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450lastatk_01.DIG', '')
        FaceSpawnLocation()
        Size(1500)
    sprite('null', 11)
    sprite('null', 4)


@State
def __450_lastAtkrenzoku():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
    sprite('null', 5)
    CreateObject('450_bigmazzleShock2', -1)
    ParticleRotationAngle(50000)
    ParticleSize(2400)
    CallCustomizableParticle('blef_433hibana_add2', -1)


@State
def __450_lastTame():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        LinkParticle('blef_450lasttame_circle')
        uponSendToLabel(32, 0)
        Size(2000)
    sprite('null', 32767)
    CreateObject('450_lastTame2', -1)
    SetScaleSpeed(-10)
    label(0)
    sprite('null', 10)
    TriggerUponForState('450_lastTame2', 32)
    ConstantAlphaModifier(-26)


@State
def __450_lastTame2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        LinkParticle('blef_450lasttame_speed')
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def __450_Nokoribi():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450nokoribi.DIG', '')
        FaceSpawnLocation()
    sprite('null', 28)
    ConstantAlphaModifier(-10)


@State
def __450nageBG():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
    sprite('null', 32767)
    LinkParticle('blef_450ahbg2_01')
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def __450_rock():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450rock.DIG', '')
        IgnoreFinishStop(1)
    sprite('null', 15)
    CreateParticle('blef_450minirock01', -1)
    sprite('null', 30)
    CreateObject('450_rock00', -1)
    sprite('null', 30)
    AlphaValue(0)


@State
def __450_rock00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Flip()
        Eff3DEffect('bl_450rock.DIG', '')
        IgnoreFinishStop(1)
        Size(1500)
    sprite('null', 10)
    CreateParticle('blef_450minirock01', -1)
    sprite('null', 49)
    CreateObject('450_rock01', -1)


@State
def __450_rock01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Eff3DEffect('bl_450rock.DIG', '')
        IgnoreFinishStop(1)
        Size(600)
    sprite('null', 59)


@State
def HeatUpEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        LinkParticle('blef_lvupsub')
        E0EAEffectPosition(2)
    sprite('null', 65)
    CreateParticle('blef_lvup_hinoko', -1)
    PrivateSE('blse_08')


@State
def __440_frameEffEX():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreFinishStop(1)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        AddX(-250000)
        Size(1600)
    sprite('vrblef440_00', 3)
    SetScaleSpeed(10)
    CreateParticle('blef_440_rock', -1)
    sprite('vrblef440_01', 3)
    CreateObject('440_Brust', -1)
    sprite('vrblef440_02', 3)
    CreateObject('440_frameEffSub', 0)
    IgnoreFinishStop(0)
    IgnorePauses(2)
    ScreenShake(8000, 8000)
    sprite('vrblef440_04', 3)
    CreateObject('440_frameEffSub2', -1)
    TriggerUponForState('440_frameEffSub', 32)
    sprite('vrblef440_05', 3)
    sprite('vrblef440_06', 3)
    sprite('vrblef440_07', 3)
    sprite('vrblef440_08', 2)
    sprite('vrblef440_09', 2)


@State
def __440_frameEff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreFinishStop(1)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        AddX(-250000)
        Size(1200)
    sprite('vrblef440_00', 3)
    SetScaleSpeed(10)
    CreateParticle('blef_440_rock', -1)
    sprite('vrblef440_01', 3)
    CreateObject('440_Brust', -1)
    sprite('vrblef440_02', 3)
    CreateObject('440_frameEffSub', 0)
    IgnoreFinishStop(0)
    IgnorePauses(2)
    ScreenShake(8000, 8000)
    sprite('vrblef440_04', 3)
    TriggerUponForState('440_frameEffSub', 32)
    sprite('vrblef440_05', 3)
    sprite('vrblef440_06', 3)
    sprite('vrblef440_07', 3)
    sprite('vrblef440_08', 2)
    sprite('vrblef440_09', 2)


@State
def __440_Brust():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Size(1350)
        Eff3DEffect('bl_430bom_00.DIG', '')
        FaceSpawnLocation()
        RotationAngle(-35000)
        AddX(150000)
    sprite('null', 3)
    AlphaValue(0)
    sprite('null', 5)
    AlphaValue(255)
    SetScaleSpeed(20)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def __440_frameEffSub():

    def upon_IMMEDIATE():
        BlendMode_Add()
        IgnoreFinishStop(1)
        SetScaleX(1600)
        SetScaleY(1600)
        SetScaleZ(750)
        RemoveOnCallStateEnd(2)
        LinkParticle('blef_440bloom_00')
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    SetScaleSpeed(60)
    ConstantAlphaModifier(-26)


@State
def __440_frameEffSub2():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        RotationAngle(50000)
        AddX(100000)
        LinkParticle('blef_433hibana_add2')
    sprite('null', 20)
    ParticleFacing(1)
    ParticleSize(1300)
    CallCustomizableParticle('blef_440_fireroad', -1)
    SetScaleSpeedY(-15)
    physicsXImpulse(-20000)
    physicsYImpulse(20000)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def EventCKRun():

    def upon_IMMEDIATE():
        LoadSpritePalette(1)
        ContinueState(600)
        physicsXImpulse(-12200)
    label(0)
    sprite('ctk450_25', 7)
    sprite('ctk450_26', 7)
    sprite('ctk450_27', 7)
    sprite('ctk450_28', 7)
    loopRest()
    gotoLabel(0)


@State
def EventTG():

    def upon_IMMEDIATE():
        LoadSpritePalette(0)
        uponSendToLabel(32, 1)
        XPositionRelativeFacing(-50000)
        SetZVal(1000)
    sprite('tg620_02', 32767)
    label(1)
    sprite('tg072_00', 14)
    CreateParticle('ef_exhit_sub', 0)
    CommonSE('100_hit_grap_3')
    sprite('tg072_00', 7)
    physicsXImpulse(-50000)
    physicsYImpulse(20000)
    setGravity(2000)
    sprite('tg072_01', 7)
    sprite('tg072_02', 7)
    sprite('tg072_01', 7)
    sprite('tg072_02', 7)
    sprite('tg072_01', 7)
    sprite('tg072_02', 7)
    loopRest()
